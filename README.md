# 使い方

1.headerのkidをアサーション署名キーに変更してください。  
2.payloadの"iss"と"sub"を自分のチャネルIDに変更してください。  
3.privateKeyにLINE Developersコンソールから発行したJSONの"privateKey"を指定してください。  
4.実行すればJWTが完成します。  
5.テストアプリでチャネルアクセストークンが発行できるか試してみましょう  
http://myucy.herokuapp.com/oauth2/v2.1/token  