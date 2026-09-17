SIG: ja-JA Localization (SIG Communications)
Date: 2026-09-16
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Kota Sakuma (Cloud Ace)** 01:34 こんにちは。
読みました。
**Yoshi Yamaguchi (Raintank, Inc. – Grafana Labs)** 01:57 あ、こんにちは。
ミュートなした。
どうでした。
**Kota Sakuma (Cloud Ace)** 02:04 めちゃくちゃ面白かったです。
**Yoshi Yamaguchi (Raintank, Inc. – Grafana Labs)** 02:05 面白かったです。か？よかったです。
**Kota Sakuma (Cloud Ace)** 02:10 めっちゃプラクティカルに書かれてて すぐ実践できそうなところ。めちゃくちゃあったんですけど、 一方で、なんか、 なんていうか求められる背景知識めちゃくちゃあるなっていうの。
**Yoshi Yamaguchi (Raintank, Inc. – Grafana Labs)** 02:27 そうっすよね。
**Kota Sakuma (Cloud Ace)** 02:30 そうなんですよ。
僕も今なんか組織でオブザバビリティなんか推進してくってなったら どう入れていくのがいいのかなっていうのはめちゃくちゃ考えましたね。
**Yoshi Yamaguchi (Raintank, Inc. – Grafana Labs)** 02:44 ね。難しいっすよね。
だから今度はそういう本の方がいいのかなと思いました。
**Kota Sakuma (Cloud Ace)** 02:52 あーなるほど。
**Yoshi Yamaguchi (Raintank, Inc. – Grafana Labs)** 02:53 その形走とかを始めるとか。
あと今月末ええと、9月の25日、 プラットフォームエンジニアリング会議っていうので。
**Kota Sakuma (Cloud Ace)** 03:06 はい。はいはい。
**Yoshi Yamaguchi (Raintank, Inc. – Grafana Labs)** 03:07 それに関連の話をするんですよ。その。
**Kota Sakuma (Cloud Ace)** 03:10 はい。はい。
**Yoshi Yamaguchi (Raintank, Inc. – Grafana Labs)** 03:10 チームでオブザビリティの基盤を。
チームっていうか組織か 入れようと思っときに、まあよくあるのは、 こう、中央のチームがなんか。
あの 頑張ってやるんだけど、結果開発チームがなんかこうちょっと気に食わねえって言ってどんどんカスタマイズしててはたはめつつ。
**Kota Sakuma (Cloud Ace)** 03:37 めちゃくちゃそれます。
**Yoshi Yamaguchi (Raintank, Inc. – Grafana Labs)** 03:40 なので、そうじゃなくて 最小限のこうパッケージとかガイドラインを作って自分でやりやすくするようにしたら いいじゃん。みたいな。
そういう話をしようと思ってるんですけど、スライドは 今から作んなきゃいけないんで。
**Kota Sakuma (Cloud Ace)** 04:01 めちゃくちゃハードですね。
**Kazunori Otani** 04:04 おはようございます。
**Kota Sakuma (Cloud Ace)** 04:07 ありがとうございます。
**Yoshi Yamaguchi (Raintank, Inc. – Grafana Labs)** 04:08 なのか。
**Kazunori Otani** 04:09 今はなんだっけ？どのイベントの話。
**Yoshi Yamaguchi (Raintank, Inc. – Grafana Labs)** 04:13 プラットフォーム。エンジニアリング、会議。
**Kazunori Otani** 04:16 結構すぐじゃないですか。もう。
**Yoshi Yamaguchi (Raintank, Inc. – Grafana Labs)** 04:18 そうだよ。
**Kazunori Otani** 04:19 はい、お疲れ様です。
**Yoshi Yamaguchi (Raintank, Inc. – Grafana Labs)** 04:23 いやまあ先週強姦はするだったかね。
もうあのない、もう自転車操業なんですよ。私は。
**Kazunori Otani** 04:33 はい。
**Yoshi Yamaguchi (Raintank, Inc. – Grafana Labs)** 04:34 はい。
**Kazunori Otani** 04:35 自転車屋さん。
**Yoshi Yamaguchi (Raintank, Inc. – Grafana Labs)** 04:37 自転車屋さん、 そうですよ。だって25日終わった後になんかジャガーのよくわかんないイベントが。
**Kazunori Otani** 04:44 ありますね。
**Yoshi Yamaguchi (Raintank, Inc. – Grafana Labs)** 04:45 あるんで、 全然そういうイベントだって聞いてなくて、ふたを開けてみたら、なんかめっちゃ同業者ばっかりじゃないかみたいな。
**Kazunori Otani** 04:52 そう。
なんか同業者イベントみたいな感じだけど内容。そんな大した内容ないんですよね。正直、あの。
**Yoshi Yamaguchi (Raintank, Inc. – Grafana Labs)** 05:02 ないよ。
**Kazunori Otani** 05:04 エーアイにテレメトリを分析させるにはどうしとどうなるのかみたいな話でややればいいんじゃないすかね？ぐらいのかん話しかないんで。
**Yoshi Yamaguchi (Raintank, Inc. – Grafana Labs)** 05:13 もう、だから俺はもうね、あの、そういうなんかこうあるじゃん。各社のさ、 マネージドななんか な。んちゃらAIみたいな。
もうそういうのは そのそれについての話 それの機能についての話はしない。
**Kazunori Otani** 05:36 ええ。
**Yoshi Yamaguchi (Raintank, Inc. – Grafana Labs)** 05:37 したってしょうがないもん したってしょうがないとか言っちゃう。
**Kazunori Otani** 05:42 でも逆にどうすんん？そうしたらもう話すことなくない。
**Yoshi Yamaguchi (Raintank, Inc. – Grafana Labs)** 05:46 え、いや、だからそれをそれをどう作ってんのかって話をする。
あれ。
**Kazunori Otani** 05:55 ええ。
**Yoshi Yamaguchi (Raintank, Inc. – Grafana Labs)** 05:56 だから、そのそのユーザーに対して提供してる機能の話をしてもしょうがないから。
そのそのAI 支援ツールをどう作ってんのか。っていう会社で。
**Kazunori Otani** 06:12 なるほど。
**Yoshi Yamaguchi (Raintank, Inc. – Grafana Labs)** 06:13 それの話をする。
**Kazunori Otani** 06:14 はい。
**Yoshi Yamaguchi (Raintank, Inc. – Grafana Labs)** 06:15 なんで。
**Kazunori Otani** 06:16 これだと確かに。
**Yoshi Yamaguchi (Raintank, Inc. – Grafana Labs)** 06:17 そうだから、それは別に あくまで一。我々の企業ではこういうことを試して色々やった結果、こういう感じで プロセスやってます。とでこういうふうにこう。例えば、aiが何かを評価するっていった時には こういうような形でプロセス回してます。みたいな そういう話を。
だってね。企業。そのサービスの話したって ただのプロダクトピッチになっちゃうじゃね。
**Kazunori Otani** 06:51 そうなんですよね。で、しかも似たような感じの。
**Yoshi Yamaguchi (Raintank, Inc. – Grafana Labs)** 06:54 そうですね。
**Kazunori Otani** 06:54 が続くだろうし。
**Yoshi Yamaguchi (Raintank, Inc. – Grafana Labs)** 06:56 なんか三人目くらいになったらもう飽きたってなっちゃうと思うから。
そういう話はしない。
**Kazunori Otani** 07:03 はい。
**Yoshi Yamaguchi (Raintank, Inc. – Grafana Labs)** 07:03 あとそれで資料を作っておいて、 別のところでもっと使えるようにいろいろこう 下調べをねすると、長大な 長大なまたあの禅の仕事。
**Kazunori Otani** 07:20 とが。
**Yoshi Yamaguchi (Raintank, Inc. – Grafana Labs)** 07:20 順の本をね。書いたりとかなんだったら、普通にまた本を書いたりとかね。はいしますよ。
はい、じゃあ、まさきさんもいらっしゃったね。
じゃあまずはこれを共有するか。
ピッピッピーはいえーっと、 ラングジャーのプルリック状況どうですか？
最近はね、江田さんと 寿司本さんがいっぱい。レビューしてくれてるんで ええ、どうですかねええ。レビュー、リクエステッドが 十件ぐらいですか？
チェンジリクエステッドが370件 全部対応してるはずなんだよね。俺 全部対応してます。
ありがとうございます。
**Kota Sakuma (Cloud Ace)** 08:25 ありがとうござい。
**Yoshi Yamaguchi (Raintank, Inc. – Grafana Labs)** 08:26 でも。
**Kazunori Otani** 08:27 すごい。
**Yoshi Yamaguchi (Raintank, Inc. – Grafana Labs)** 08:28 対応してます。
**Kazunori Otani** 08:29 メール通知だけ 一応受けてるけど、すごい量が来て 流れてるなっていうところしか最近見れてなくて。
**Yoshi Yamaguchi (Raintank, Inc. – Grafana Labs)** 08:39 全部全部対応してます。
**Kazunori Otani** 08:41 あと最近。
**Yoshi Yamaguchi (Raintank, Inc. – Grafana Labs)** 08:42 ね。最近、あのほら、チャットにもコメントくださったんだけれども、 あのうタイポとかね 直してくださっている方が いるんですよ。
このジグザグデブさん、 ジグダグデブさんねこの まさとし。荻原さん。
あの 結構コンスタントにくれてますよ。ちょいちょっ。
**Kazunori Otani** 09:11 ありがたい。
**Yoshi Yamaguchi (Raintank, Inc. – Grafana Labs)** 09:12 はい、ぜひねこの調子でやっていただいて、 アップロバになっていただきましょう。
じゃあ淡々とね、やってます。っていうことで 聞くと、 あの結局行くのやめたんですけど、 やっぱシートかぶっちゃったから あの韓国の なんかこう、オープンソース関連のテーマのカンファレンスが 貼って、そこにプロポーザルを出すときに調べたんですよ。
あの日本語のあの。
なんすか？
その進捗具合。
**Kazunori Otani** 09:57 へえ。
**Yoshi Yamaguchi (Raintank, Inc. – Grafana Labs)** 09:59 だよね。結構言ってた。
結構行ってて 何パーだっけな。なんかね、結構行ってた。
なんかね、あの スクリプトが 入ってんすよ。
62。パレッジ62。パ。
**Kazunori Otani** 10:21 まあまあ。
**Yoshi Yamaguchi (Raintank, Inc. – Grafana Labs)** 10:23 すごくない。
**Msk Msk** 10:26 ブログ含めてですか？
**Yoshi Yamaguchi (Raintank, Inc. – Grafana Labs)** 10:27 ブログ含めて。
**Msk Msk** 10:28 やば。
**Yoshi Yamaguchi (Raintank, Inc. – Grafana Labs)** 10:33 あのこれね、スクリプトがあってえっとなんだっけ ええ。オー。プンテレメトリIOの えっとね。
スクリプツの アイレIATN。のあ違うなぁなんかねチェ。ッ。クかどっかにね。
あらあらあら、この辺だ。
ここのあ、違うなぁ。
どっかのね。パールの そう、パールのスクリプトがて、そこに ギタークションかなぁ。
ギターはアクションのスキュリプトかな？
違うな。まあどっかにあるっす。パールのスクリプトがそれでチェックできますよ。
**Msk Msk** 11:26 すげー。
**Yoshi Yamaguchi (Raintank, Inc. – Grafana Labs)** 11:29 はいということ。
**Msk Msk** 11:31 なんでポール。
**Yoshi Yamaguchi (Raintank, Inc. – Grafana Labs)** 11:32 でも結構パールあるんだよ。結構パールある。ほら。
**Msk Msk** 11:36 チャリンの趣味。
**Yoshi Yamaguchi (Raintank, Inc. – Grafana Labs)** 11:37 チャリンの趣味チャリンの趣味の可能性はありますね。
とりあえず 書こうと思ってパール書いちゃうみたいな。
はい、 そういうことでした。ちょっと後でどっか共有しておきますね。
次ええ。イベントね。
イベントあとこれもありますよ。これも これもね、ありますから、 これが11月の 28、29 だったと思います。あ、18、19かありますね。
これこれあります。
これが10月1日。
これがこれがこっちの方が速い。
9月25。
入力か26です。
あとはあれね、オープンソースサミットね。
オープン。
オープンソースサミットジャパン。
これが12月の789。
もうね、年末が見えてきましたよ。はやっ。
**Kazunori Otani** 13:03 はい。
**Yoshi Yamaguchi (Raintank, Inc. – Grafana Labs)** 13:04 気がついたらもう一年終わっちゃうよ。
最悪だ。
ええ。
他なんかありますか？
**Kazunori Otani** 13:24 あと、なんかスペック翻訳仕様みたいな話提案した。としてたのってここ一ヶ月でしたっけ。
**Yoshi Yamaguchi (Raintank, Inc. – Grafana Labs)** 13:31 だと思だと思うなぁ。
で、なんかそれはこの オープンテリメトリドットioの範疇じゃな。い。から あのスペックの ほうのに言えっつって言われて。で面倒くせえなって思って 辞めてる。
これですね。
ええ。三。週間前。
これオッケーってとこはい。
**Kazunori Otani** 14:05 まあ。
**Yoshi Yamaguchi (Raintank, Inc. – Grafana Labs)** 14:06 そうですね。
スペックアテンドスペック。ミーティングスペック。ミーティンパックのタイムゾーンでやってねえじゃねえかよ。
ふざけやがって。
えっと。
使用の翻訳についてええし。
フェックシグ二周立てろ。
割れた。
でも面倒くさいんだよね。
もう勝手にやりました。
勝手に勝手にやりましたよ。
スペック。
**Kazunori Otani** 14:54 とりあえず。
**Yoshi Yamaguchi (Raintank, Inc. – Grafana Labs)** 14:56 とりあえずここに全部あります。
私のウェブサイトにあります。
でー、ほか えっと、先月出た。このこれね、これやりたいですね。
くばれて。その。
なんかこのアップストリームトレーニングみたいなやつ。
これあれ？佐久間さん。
先月のミーティングいったんでしたっけ？
**Kota Sakuma (Cloud Ace)** 15:31 はい。
**Yoshi Yamaguchi (Raintank, Inc. – Grafana Labs)** 15:33 そうね。佐久間さんはいた。
佐久間さんは 加ちゃん。これ知ってる？
**Kazunori Otani** 15:42 知らない。
**Yoshi Yamaguchi (Raintank, Inc. – Grafana Labs)** 15:43 なんかアップストリームトレーニングって言ってて、なんかそのアップストリームに 貢献する何かを やり方を教えます。みたいなコントリビューションを教えますみたいな そういう感じなんだけど、 なんかそれと並行してこのドッグスプリントっていうのがあって、なんか？
この 桑年鉄の日本語ドキュメントにみんな貢献しようぜ。みたいな。
そういうのやってんすよこれ。
なので、似たようなことをやれば いいんじゃないかなって思いました。
**Kazunori Otani** 16:22 はいと言いながら、なんか今のペースだと そんなに人ま。
**Yoshi Yamaguchi (Raintank, Inc. – Grafana Labs)** 16:31 俺が俺がね、やり続ければ終わっちゃうよ。
**Kazunori Otani** 16:35 そうそう。
**Yoshi Yamaguchi (Raintank, Inc. – Grafana Labs)** 16:36 それもどうかなと思で、 私もそう新しいのをやめて。
**Kazunori Otani** 16:41 だから目的としてはペース上げるっていうよりは他の。なんか。
**Yoshi Yamaguchi (Raintank, Inc. – Grafana Labs)** 16:47 そう。
**Kazunori Otani** 16:47 いろんな人を巻き込んだ方がいいよねっていう。
**Yoshi Yamaguchi (Raintank, Inc. – Grafana Labs)** 16:49 そうそうそうそうそう。
**Kazunori Otani** 16:52 おっしゃることはわかる。
**Yoshi Yamaguchi (Raintank, Inc. – Grafana Labs)** 16:54 はいええ。
**Kazunori Otani** 16:59 あのペースでやっちゃったらね。多分。
**Yoshi Yamaguchi (Raintank, Inc. – Grafana Labs)** 17:02 まーあの。
本体自体はずっとこう アップデートされていくんであの新しい。のの追加じゃなくてアップデートするのも結構大変だから。
それはそれで 全然やることはずっとあり続けるんだけれども、 まあ新しいのって結構ボリュームあるんでね。
なので、まあなくなりはしないんだけど、まあ新しい人がどんどん入ってくれた方がいいかなと思で。
**Kazunori Otani** 17:31 はいいと思います。
**Yoshi Yamaguchi (Raintank, Inc. – Grafana Labs)** 17:48 これはなんかオンラインでやるでもいいですしオフラインでもいいんですけど、 なんかどうですか？
皆さんは。
というホストしてもいいよっていう 人いますか？
佐久間さんとか。
**Kota Sakuma (Cloud Ace)** 18:11 具体的に何かホストするってなったら 僕は全然その動き方を見えてない。
**Yoshi Yamaguchi (Raintank, Inc. – Grafana Labs)** 18:18 まあまあイベントの募集云々かんのは、まあ僕らも全然お手伝いするとして、多分当日の その 当日のフローっていうのは多分大事だと思ですよね。
で、そのこれちょっと大きくするか あれこれあと聞く。なんだっけ？
表示。
**Kazunori Otani** 18:44 まぁ一旦大丈夫。
**Yoshi Yamaguchi (Raintank, Inc. – Grafana Labs)** 18:51 こう。この回は二時間くらいやってるんですけど。
多分そのコントリビュートするん いろいろ決まりがあるじゃないですか。
それをまあ簡単に紹介して。
でみんなにこう翻訳されてないページを探してもらって で質問ある？とかよくやり方わからないっていう人には 教習してもらったりとかしてこうですって言って。
で、こうリクエスト作ってもらえれば ここに載るはず。なんで ここに載ってたのをこう。我々アップルア以上の人たちが はい、よくできましたって言って 確認してマージして 貢献できました。バシバシバシみたいな。
そういうイベントになると思われます。
**Kota Sakuma (Cloud Ace)** 19:53 本当にその。なんかコントリベートの手順をなぞるみたいな イメージなんですかね？
**Yoshi Yamaguchi (Raintank, Inc. – Grafana Labs)** 19:58 最初はそうっすね。で、なんかその、多分どういう風にこう。
訳語とかニュアンスとかがよくわからないです。っていう人もいたりすると思で、 時にこう こんな感じです。って 教えてあげるくらいですかね？
それくらいです。
イベントとかは、まあ、 オープンテレメトリーのこのコンパスがあるんで、 コンパスで募集したりすればいいんじゃないかと思っています。
すごいじゃん。メンバー1300人もいるじゃん。
**Kazunori Otani** 20:44 すごい。
**Yoshi Yamaguchi (Raintank, Inc. – Grafana Labs)** 20:45 びっくりした。今気づいてびっくりした。
**Kazunori Otani** 20:50 あと、そういえば名古屋でミートアップやろうみたいな話ありましたね。
**Yoshi Yamaguchi (Raintank, Inc. – Grafana Labs)** 20:54 あれはどうなったんだ。
**Kazunori Otani** 20:55 あれ、どうもなってないと思う。
**Yoshi Yamaguchi (Raintank, Inc. – Grafana Labs)** 20:58 やらなかったら誰もやらないぞ。
**Kazunori Otani** 21:02 ええ。
そうじゃなくてもなんかそろそろミトアップ企画ししてもいいなみたいな タイミングにはなってきましたよね。そういえば。
**Yoshi Yamaguchi (Raintank, Inc. – Grafana Labs)** 21:13 そうですね。
前回が5月でしょ。
そろそろやってもいいんじゃないですか？
**Kazunori Otani** 21:21 ね。なんか喋る人いれば、 あとは場所とかはまあ適当にやるとして。
**Yoshi Yamaguchi (Raintank, Inc. – Grafana Labs)** 21:30 何人くらい始まるのかなぁ。
**Kazunori Otani** 21:37 なんか喋ってほしい人とかいます。関連で。
**Yoshi Yamaguchi (Raintank, Inc. – Grafana Labs)** 21:43 関連 そうだなあ。
あんまり あんまり思いず思い思い浮かばないなあ。
まさきさんは眠そうですね。
**Msk Msk** 22:25 ちょっと 会社のミーティングを流しながったんでずっとミュートだった。
**Yoshi Yamaguchi (Raintank, Inc. – Grafana Labs)** 22:32 感じなんではい。
**Msk Msk** 22:36 いつかリスケお願いするかもしれない。
**Yoshi Yamaguchi (Raintank, Inc. – Grafana Labs)** 22:39 い。つか。
**Msk Msk** 22:40 いつかいや、わかんない。この会社のミーティングがあの定期的にこの時間だったら困るなと思って。
**Yoshi Yamaguchi (Raintank, Inc. – Grafana Labs)** 22:45 ああ。確かに。
**Msk Msk** 22:46 とこれなくなっちゃで、ちょっとなんかいつかリスケをお願いするかも。
**Yoshi Yamaguchi (Raintank, Inc. – Grafana Labs)** 22:49 そうっすね。
Aあとはなんですか これいつって書いてあるの？これこれ これはそのまま残ってんじゃん。
**Kazunori Otani** 23:02 そうですね。
**Msk Msk** 23:10 来年のオブザビリティ。こんなキックオフをしようっていう話を二回ぐらい聞いて。
**Kazunori Otani** 23:15 はい、そういえばそれもありますもんね。
**Msk Msk** 23:17 スコードとスラックで観測して流れたなって。
**Kazunori Otani** 23:21 はい、 とりあえず とりあえずビール飲む会でもしますか？
とりあえず、 え。佐久間さんってどこに住んでるんですか？
**Kota Sakuma (Cloud Ace)** 23:42 奥にあみです。
**Kazunori Otani** 23:44 宮城。そう、逆に来れる距離かなと思って確認をしようとしたら。
**Kota Sakuma (Cloud Ace)** 23:51 そうなんです。お土産なんです。
**Kazunori Otani** 23:53 はい。
まあ、気楽に来れる距離かどうかはちょっと人によると思うけど。
**Kota Sakuma (Cloud Ace)** 23:58 東京なら全然全然行けますってくらいですかね？
**Yoshi Yamaguchi (Raintank, Inc. – Grafana Labs)** 24:02 全然ってほどでもないでしょ。
宮城は。
**Kota Sakuma (Cloud Ace)** 24:06 全然ですよ。まだまだ。
**Yoshi Yamaguchi (Raintank, Inc. – Grafana Labs)** 24:09 えなん？どれぐらいかかるんですか？
**Kota Sakuma (Cloud Ace)** 24:11 言うてでも二時間ぐらいですかね。場所にももちろんよりますけど。
**Kazunori Otani** 24:17 まぁちょっと三時間。
**Yoshi Yamaguchi (Raintank, Inc. – Grafana Labs)** 24:18 東京駅で二時間。
**Kota Sakuma (Cloud Ace)** 24:20 東京駅で二時間あったら行けますかね？
**Yoshi Yamaguchi (Raintank, Inc. – Grafana Labs)** 24:24 マジ俺うちと変わんないじゃん。
**Kota Sakuma (Cloud Ace)** 24:27 確かにそうなんですか。
**Kazunori Otani** 24:30 甲府新宿でだいたい一時間半だしね。
**Yoshi Yamaguchi (Raintank, Inc. – Grafana Labs)** 24:34 そう、甲府から東京駅のあの直行の 梓沙会場もあるんだけど、それで一時間45。
**Kota Sakuma (Cloud Ace)** 24:44 意外と新幹線使うと 意外と埼玉の人とかより早かったりする時ありますね。
**Kazunori Otani** 24:50 ええ。
**Yoshi Yamaguchi (Raintank, Inc. – Grafana Labs)** 24:53 そうなんですよ。これから。
**Kazunori Otani** 24:55 とりあえずじゃあまじで。
**Yoshi Yamaguchi (Raintank, Inc. – Grafana Labs)** 24:59 もしえ？あれ？ちなみにマサキさんは どこなんでしたっけ？
**Msk Msk** 25:06 私は全然バリバリ東京です。
**Yoshi Yamaguchi (Raintank, Inc. – Grafana Labs)** 25:08 バリバリ東京もさ、ほら、東西に広いから。
**Msk Msk** 25:11 文京区の方に住んでます。
**Yoshi Yamaguchi (Raintank, Inc. – Grafana Labs)** 25:13 文京区かー。真ん中のいやだからそのまさきさんが、もし西側だったらね。
**Msk Msk** 25:19 あー。
**Yoshi Yamaguchi (Raintank, Inc. – Grafana Labs)** 25:20 わざわざ東京の都心まで出なくても、もっと西側で だったらをベスト。
**Kazunori Otani** 25:30 いや、でも宮城から。
**Yoshi Yamaguchi (Raintank, Inc. – Grafana Labs)** 25:33 宮城から来れないからね。
来れない日程なんだったら そっちの方が 俺とか買っちゃうもん。助かるでしょ。
**Kazunori Otani** 25:42 あ、でもあれなんだっけ？
浦和乗り換えで武蔵野線で。
**Yoshi Yamaguchi (Raintank, Inc. – Grafana Labs)** 25:48 超回るじゃん。
情報は悪い。
**Kazunori Otani** 25:52 なくはないですよね。
**Kota Sakuma (Cloud Ace)** 25:53 あれからなくはないから。
確かに、確かに。
**Kazunori Otani** 25:59 はい。
**Yoshi Yamaguchi (Raintank, Inc. – Grafana Labs)** 26:00 浦和通るんだっけ？東北新幹線って。
**Kota Sakuma (Cloud Ace)** 26:03 エラーは直接は取れないですけれど。
**Kazunori Otani** 26:05 浦和じゃなくてなんだっけ？大宮か。
**Kota Sakuma (Cloud Ace)** 26:07 大宮ですね。
**Yoshi Yamaguchi (Raintank, Inc. – Grafana Labs)** 26:08 大宮通り。
**Kazunori Otani** 26:09 大宮から一回乗り換えて、武蔵野線で立川。
**Yoshi Yamaguchi (Raintank, Inc. – Grafana Labs)** 26:16 超い。
**Kazunori Otani** 26:17 そう。
**Yoshi Yamaguchi (Raintank, Inc. – Grafana Labs)** 26:18 いけた気がしますね。
**Kazunori Otani** 26:21 大宮から多分三四十分ぐらいかな。確か。
**Yoshi Yamaguchi (Raintank, Inc. – Grafana Labs)** 26:25 びっくりするのやつじゃん。
はい。
**Kazunori Otani** 26:29 立川。
立川。
ミートアップミートアップ。
確かビール会やりますか？
**Yoshi Yamaguchi (Raintank, Inc. – Grafana Labs)** 26:37 立川は結構暑いね。
結構暑い。
一時間ぐらいで着いちゃうもんね。
**Kazunori Otani** 26:48 まあ、なんかカジュアルにこの辺なんか 気運を盛り上げるのはちょっと していいかなという気はしましたので、 あとは何人か声かけて、 もしくはオブザビリティカンファレンスのコミュニティでも、なんか 急にとりあえず飲みましょうみたいな感じで やってもいいのかもしれないですね。
**Yoshi Yamaguchi (Raintank, Inc. – Grafana Labs)** 27:25 そういえば思いだしたな。
**Kazunori Otani** 27:26 っていうノリでやってますけど、佐久間さん的には大丈夫ですか？こんなノリで。
**Kota Sakuma (Cloud Ace)** 27:32 僕はもう呼ばれたら呼ばれたら行きます。
**Kazunori Otani** 27:34 あ、じゃあもう全然よく。でも行きます。
**Yoshi Yamaguchi (Raintank, Inc. – Grafana Labs)** 27:37 はあの、なんか 東京に来る機会はあるんですか？
**Kota Sakuma (Cloud Ace)** 27:45 今はあんまりないんですよね。なかなかなので、呼ばれたタイミングでという感じにはなりますかね。
**Yoshi Yamaguchi (Raintank, Inc. – Grafana Labs)** 27:53 なるほど。
**Kazunori Otani** 27:55 なんかよくあるパターンがね。旅費とか 出張扱いで出るタイミングに合わせてみたいなのはまあよくあるたパターン。
機械があれば もうそれで調整すればいいし っていう感じですよね。
エンドユーザーシグ周り。
**Yoshi Yamaguchi (Raintank, Inc. – Grafana Labs)** 28:25 あのクボンで撮った動画を元にした ブログポストを書いて、 それを今レビューしてもらっっています。
**Kazunori Otani** 28:43 素晴らしい。
**Yoshi Yamaguchi (Raintank, Inc. – Grafana Labs)** 28:44 はい。今動画が編集中なので、動画が来れば その動画をここら辺に埋め込んで。
で、それがブログになります。
**Kota Sakuma (Cloud Ace)** 29:02 そうそう。
**Kazunori Otani** 29:02 動画のあ、動画の編集って誰がどういう風にやってるんですか？
**Yoshi Yamaguchi (Raintank, Inc. – Grafana Labs)** 29:06 で、なんかエンドユーザーシグのこういうコメントがあるんだけど、エンドユーザーシグの。
**Kazunori Otani** 29:14 てき。
**Yoshi Yamaguchi (Raintank, Inc. – Grafana Labs)** 29:15 ここじゃねえな。ええ、これだ。
**Kazunori Otani** 29:18 何かやってくれるんだ。
**Yoshi Yamaguchi (Raintank, Inc. – Grafana Labs)** 29:20 これのここにある。
ええ、このね。
**Kazunori Otani** 29:25 グーグルドライブに上げてみたいな感じなんだ。
**Yoshi Yamaguchi (Raintank, Inc. – Grafana Labs)** 29:29 このソフィー ソフィーさん。
この人が今やってくれてますね。
**Kazunori Otani** 29:35 ええ。素晴らしい。
**Yoshi Yamaguchi (Raintank, Inc. – Grafana Labs)** 29:37 はい。
**Kazunori Otani** 29:38 はい。
**Yoshi Yamaguchi (Raintank, Inc. – Grafana Labs)** 29:40 はい。
ヒューマンズ。オブ。オーテルのインタ ビュー動画の文字をこう。
記事正中。
はい、 そんな感じですね。
**Kazunori Otani** 30:14 じゃあ引き続きと言いつつ、 キックオフの懇親はじゃあ適当に しますね。一旦呼びかけをあと坂西先生に呼びかけてって呼びかけるのも ありかな。
**Yoshi Yamaguchi (Raintank, Inc. – Grafana Labs)** 30:39 今も声は途切れちゃった。
**Kazunori Otani** 30:41 坂西先生に呼びかけてってお願いする。
まあいいやはい、ちょっと10月 来週とかはさすがに急すぎますよね。例えば。
**Yoshi Yamaguchi (Raintank, Inc. – Grafana Labs)** 30:57 いや、私は無理やなあ。
**Kazunori Otani** 30:59 ね。まあ10月中ぐらいでちょっと考えますか。
**Yoshi Yamaguchi (Raintank, Inc. – Grafana Labs)** 31:04 なんか なんかのついでとかだとすごい助かるけれども。
**Kazunori Otani** 31:09 逆にこの日がいいとかあればそれ軸に調整します。
**Yoshi Yamaguchi (Raintank, Inc. – Grafana Labs)** 31:15 なるほど。
**Kazunori Otani** 31:16 はい。
**Yoshi Yamaguchi (Raintank, Inc. – Grafana Labs)** 31:17 了解です。
**Kazunori Otani** 31:18 ちょっとまたスラックディスコードその他で調整しましょう。
はい。
**Yoshi Yamaguchi (Raintank, Inc. – Grafana Labs)** 31:24 じゃあ私は。
**Kazunori Otani** 31:26 仕事に戻ります。
**Yoshi Yamaguchi (Raintank, Inc. – Grafana Labs)** 31:28 はい。
**Kazunori Otani** 31:29 はい。
**Yoshi Yamaguchi (Raintank, Inc. – Grafana Labs)** 31:32 他に何かある方いれば続けます。しなければこれでおしまいにします。
**Kota Sakuma (Cloud Ace)** 31:39 大丈夫です。
**Msk Msk** 31:40 大丈夫です。
**Yoshi Yamaguchi (Raintank, Inc. – Grafana Labs)** 31:41 はい、じゃあ終わりにしましょう。はい、また来月。
**Msk Msk** 31:45 はい、お疲れ様です。
**Yoshi Yamaguchi (Raintank, Inc. – Grafana Labs)** 31:47 です。
