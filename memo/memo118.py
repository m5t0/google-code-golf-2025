def p(p):
    # 2の座標を取ってくる
    t = {(l, n) for l in range(len(p)) for n in range(len(p[0])) if p[l][n] & 2}
    # iは十字方向に通るマス
    # 2の座標をすべてlが含むのであればlを返す
    # そうでない場合
    # - iが空でないのであればiからi[0]を除いた場合を考える
    # - lからi[0]を除いた集合が空でないのであれば、i[0]をlに移した集合を考える
    d = lambda i, l: [i and (d(i[1:], l) or not i[0] & l and d(i[1:], l | i[0])), l][
        # 2の座標をすべてlが含むかどうか
        t <= l
    ]
    for n in 2, 3:
        # nマス十字方向に進むときに通るマスの集合で0を通らず2を通るもの
        l = [
            l
            # 列と行について全探索
            for d in range(len(p))
            for i in range(len(p[0]))
            for l in [
                {
                    (l, n)
                    for l in range(-n, n + 1)
                    # 縦or横にlマス進む場合のループ
                    for l, n in [(d + l, i), (d, i + l)]
                    # 長方形の外にないことをチェック
                    if len(p) > l > -1 < n < len(p[0])
                }
            ]
            # 0のマスを通らなくて2を通る
            if min(p[l][n] for l, n in l) & 2
        ]
        # 十字方向に動いたときに升目を重複している可能性があるためsetを取る
        if l := d(l, set()):
            # 確定したのでマスの色を変える
            for l, n in l:
                p[l][n] += 3 * (p[l][n] & 1)
            return p
