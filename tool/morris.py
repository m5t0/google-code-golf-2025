from zipfile import ZipFile
import zipfile
import zopfli.zlib
import zlib
import warnings

def zip_src(src_code):
    candidates=[src_code]
    for compress in[zopfli.zlib.compress,lambda d:zlib.compress(d,9)]:
        for trailing in[b'',b'\n']:
            src=src_code+trailing
            while(comp:=compress(src))[-1]==ord('"'):src+=b'#'
            for delim in[b"'",b'"']:
                esc_map={0:b'\\x00',ord('\n'):b'\\n',ord('\r'):b'\\r',ord('\\'):b'\\\\',delim[0]:b'\\'+delim}
                sanitized=b''.join(esc_map.get(b,bytes([b]))for b in comp)
                compressed=b'import zlib\nexec(zlib.decompress(bytes('+delim+sanitized+delim+b',"L1")))'
                if max(sanitized)>127:compressed=b'#coding:L1\n'+compressed
                else:print('no header needed!')
                candidates.append(compressed)
            esc_map={0:b'\\x00',ord('\r'):b'\\r',ord('\\'):b'\\\\'}
            sanitized=b''.join(esc_map.get(b,bytes([b]))for b in comp)
            compressed=b'import zlib\nexec(zlib.decompress(bytes("""'+sanitized+b'""","L1")))'
            if max(sanitized)>127:compressed=b'#coding:L1\n'+compressed
            else:print('no header needed!')
            candidates.append(compressed)
    valid_options=[]
    for code in candidates:
        try:
            with warnings.catch_warnings():
                warnings.simplefilter("ignore", category=SyntaxWarning)
                with open('tmp.py','wb')as f:f.write(code)
                with open('tmp.py','rb')as f:x=f.read()
                exec(x,{})
                valid_options.append(code)
        except:0
    return min(valid_options,key=len)

files = {}
total_save=0
with ZipFile("submission.zip", "w", zipfile.ZIP_DEFLATED) as zipf:
    for f in range(1,401):
        try:
            filename='./code/task' + str(f).zfill(3) + '.py'
            o=open(filename,'rb').read().strip()
            zipped_src = zip_src(o)
            files[f] = min(len(o), len(zipped_src))
        except:
            print('no puedo', filename)
            continue
        #https://www.kaggle.com/code/cheeseexports/big-zippa
        improvement = len(o) - len(zipped_src)
        if improvement > 0:
            print(f,improvement)
            total_save += improvement
            open('./submission2/task' + str(f).zfill(3) + '.py','wb').write(zipped_src)
        else:
            open('./submission2/task' + str(f).zfill(3) + '.py','wb').write(o)
        zipf.write('./submission2/task' + str(f).zfill(3) + '.py')
print("Total Compression Save: ", total_save)