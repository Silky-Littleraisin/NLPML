# 『ゼロから作る Deep Learning 2』


## 1章 ニューラルネットワークの復習

前作『ゼロから作る Deep Learning』の内容の復習。

前作の内容をサマライズした内容は省略するとして、差分や、要復習だった部分を書く。

* 1.3.4 計算グラフ
    * 分岐ノード
        * 逆伝播のときは、上流からの勾配の和になる
    * Repeatノード
        * 分岐ノードの一般化。逆伝播のときは上流からの勾配の総和を取る
    * Sumノード
        * Repeatノードと順伝播と逆伝播が逆になっているノード
    * MatMulノード
        * 結論は分かったが、導出過程の説明が理解が浅いように思うので、再度確認が必要
* 1.3.5.1 Sigmoid 関数の微分の導出過程
    * 詳細は「付録 A」参照
* 重みの更新
    * 更新のステップ
        * 訓練データの中からランダムに複数のデータを選び出す
        * 誤差逆伝播方式により、各重みパラメータに関する損失関数の勾配を求める
        * 勾配を使って重みパラメータを更新する
        * 上記3ステップを必要な回数繰り返す
* 1.4.3 学習用のソースコード
    * 一般的な学習の構成
        * ハイパーパラメータの設定
        * データの読み込み、モデルとオプティマイザの生成
        * データのシャッフル
        * 勾配を求め、パラメータを更新
        * 定期的に学習経過を出力()
* 1.4.4 Trainer クラス
    * `1.4.3 学習用のソースコード` をクラスにまとめたもの
    * `ch01.train_custom_loop` を `common.trainer` にまとめ
    * `fit()` を学習用のインターフェースと持たす
* 1.5.1 ビット精度
    * 経験的に精度を落とすことなく、以下の事項が知られている
        * (64ビットではなく)32ビット浮動小数の利用で充分
        * 推論に限って言えば16ビット浮動小数で充分
        * しかし、H/W側が提供しているのが32ビット演算なので、基本的に32ビットを使う。保存のときだけ容量削減のため16ビットで実施する
* 1.5.2 GPU (CuPy)
    * numpy 互換インターフェースのGPU利用版
    * 切り替えについては `common.config`、`common.np`、`common.layers`あたりを参照。
    * 4章からのコードで使えるとのことだが、対応GPUを持っていないので試せないと思う。
* 1.6 まとめ
    * ニューラルネットワークの実装では以下を作るとよい
        * 構成要素の `Layer` クラス (I/Fとして `forward` と `backward` を持つ)
        * 学習のための `Trainer` クラス (I/Fとして `fit` を持つ)
    

## 2章 自然言語と単語の分散表現

### 2.1 自然言語処理とは

本書で扱うのは

* シソーラスによる手法 (2.2 と 付録B)
* カウントベースの方法 (2.3)
* 推論ベースの手法 (word2vec) (次章)

シソーラスとカウントベースはやったことがあるので、概ねパスするかも。


### 2.2 シソーラスによる手法

コードを伴う部分は WordNet のコーパスを使って付録Bでやるとのことだが、パス


### 2.3 カウントベースの方法

一旦英文が対象



## 環境セットアップ

### 要件

* インタプリタ
    * Python 3系 (venvで環境切り出し)
* ライブラリ
    * NumPy
    * Matplotlib
    * CuPy (オプション。非NVIDIA GPUなのでインストールできない)

    
### 構築手順

### インタプリタとvenvの設定

PyCharm を使うのでその設定

* 本体メニューの「PyCharm」
* 「Preferences」
* 「Project Interpreter」
* 「Add...」
* 「New environment」

で Base Interpreter で Python 3.x 系を選択してプロジェクトルートに `venv` ディレクトリに virtualenv の設定を配置。

### ライブラリ

* インタプリタの設定にモジュールのインストールリストが出ているので
* `numpy` と `matplotlib` を選択してインストール

環境が非NVIDIA GPUなのでCuPyはインストールに失敗するのでインストールしない。


### ライブラリのバージョンの指定

`pip freeze` の出力を保存。

```
$ pip freeze > requirements.txt
```




## 参考

* 本紙
    * [oreilly-japan/deep-learning-from-scratch-2](https://github.com/oreilly-japan/deep-learning-from-scratch-2) 
