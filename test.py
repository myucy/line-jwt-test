from jwcrypto import jwk,jwt
import time

#JWTトークンの有効期限（最大30分 エポック秒で指定）
exp = (int(time.time()))+(60 * 30)

print(exp)
#発行するチャネルアクセストークンの有効期限（最大30日。秒で指定）
token_exp = 60


header = {"alg": "RS256","typ": "JWT","kid": "1dab2f4f-b73f-47a3-b99d-1730e22b9544"}

payload = { "iss": "1573163733", "sub": "1573163733", "aud": "https://api.line.me/", "exp": exp, "token_exp": token_exp }


#LINE Developersコンソールで発行するプライベートキー。"privateKey"の中身だけなので注意
privateKey = {
    "p": "_mMa1ShoEgeQ0_bo8c1aLa626TQMEu9Ey6ecpgF1Ln_l9jwfPz0JNpJudHF0ZI_Jx6kYp1xNCO4mQpybz-d8N49tcLS9fsQ0IxfVuqJo92vDOT6JLji-l1ssN-Gw052yxtfbLAh21k_HahtEDQyXrASA1LQcFyuxcBpzuzqw6r8",
    "kty": "RSA",
    "q": "0ofg_iiqc-mwy95Jj2hh2YY5GfL-Zz1t9IZ2fUeTl1kNlt9njiW3nkrFP0sQWTXLo7ukyfph6-KhbmBGSgKGCarOFz-HbLpKevEB-zpHfvOYclYmSiBof__PudcTel67VyGH7zPfs5pF3ZZLzJ3pV9dQATgqNpa3EO4g2tFSU6k",
    "d": "rhMe1_FEp1luwTsjvtAwBXxfN4rkJ-Q92r3jHXSDj-yRNA8Drv5xEtEwFOBeJttEdiMeknsGctr3hKOxetxUl8H_XBamfxjzLw8XdZXa-ul60lveMaTrhZ_G8PwygP2AXgNR6_i08kk1QS5cAltpyCzt9kF8S6a67WdVwTvwuB_CR5cTTRGHuvdMt2klrIYZDsDZVD0bqaBmpAPKHyQtCNGgqVHTbzEVydAykbYKoHLK1-e9CViQFIJU_KeNJdTEcWy43HGmbColrbXki1yPIPLydRuSlihoJQ11fikIbaU2gC_79IeSfC5mu4kedTpwEpwOAkviZeV_pJP8YTYKwQ",
    "e": "AQAB",
    "use": "sig",
    "kid": "1dab2f4f-b73f-47a3-b99d-1730e22b9544",
    "qi": "hVkG582RG4xBesEEmCEUBdT-SpysjZ3QPHPDWI8Wm-FnnJs7K5ECmUpSkIbY4yfzBp7OZ9dyeP_iX-1iSyfLEECjDQIdAiGxLL_9ogCbl53IS_ezMRBCox9g0nf9aJ9eH3gxKCYKv3iJ2YwRilH9uNFTmH3wqYZGsvPsyARNjUE",
    "dp": "zSc1u5Qzod6yIQ9uO5uFz3OolZfg6OBH1godng9s5oxE8_j2pjReGsGrDIN2_6aqbzfi5w3cHoiZGH1edyPTnKcx9oP8kqA-_9I4DqTuDCO_NIpHbZxbsIrZtVNxHKiARjZMzk0hMaLzSpIkpnVyWErlbyS1xsX4-lSK4wLpLNc",
    "alg": "RS256",
    "dq": "SJSzyqu2aBPO8doGvjwcT-PoV7vgXTNebwjUXMiKZ4k6GCOZDfaO4TGh4vo7_qV_OUl9vGxnyezt_qGOWgGYuEh8mKM8Sw3Gk6_3IOessmXEztZIiRG3NTm6IbW2b1-tcpKKzLqzirXLFGO2aiqewbvnRyRX2U4Ievu9s_KqUVE",
    "n": "0TRR2UfFrbS6oL-PAN0Mefb4meBlMFFMSkQA9F_sMPk5-HPIohnzkyxsajXU9Q8hwCcnx3xe7nMB5QzHakqyONpiMyRPWFkErP5IxI4dQnnlWnKCuHOoscSIaB6pegm7vWShfLeAqXGV9AlgM-_oboVj0eD0BmYSAjn2sFVC2ZIi0weE2CCcRZCaXMOgPStjj5GnRusntvEh4jkivFd9q21jvBcAd3Lx8irg1M0hxrK_Uy0Larod-1xrfF6NH5dhnGjCVyDSxaWguBhpPC4xS6HXOJbLX67F2NxCS9Qz9B6EmjHLzqwpYCaRoazQs4C4gfHs4XLZLOXHcR2YOxTlFw"
}

#プライベートキーをJSONからJWKに変換
privateKey = jwk.JWK(**privateKey)

#JWTトークンを作成
Token = jwt.JWT(header=header,
claims=payload)

#作成したプライベートキーで署名
Token.make_signed_token(privateKey)

#シリアライズ
JWTtoken = Token.serialize()

#完成
print(JWTtoken)