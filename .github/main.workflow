workflow "Serverless deploy" {
  on = "push"
  resolves = ["serverless deploy"]
}

action "serverless deploy" {
  uses = "serverless/github-action@master"
  secrets = [
    "AWS_ACCESS_KEY_ID",
    "AWS_SECRET_ACCESS_KEY",
  ]
  args = "deploy"
}
