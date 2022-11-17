ssh -i ./LightsailDefaultKey-us-east-1.pem ubuntu@2600:1f18:1dde:1300:ffde:ed88:b4a5:5e66

chmod 600 ./tat-project-key.pem
ssh -i ./tat-project-key.pem  ubuntu@107.20.241.137
