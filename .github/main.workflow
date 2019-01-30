workflow "Serverless deploy" {
  on = "push"
  resolves = ["serverless deploy"]
}

action "serverless deploy" {
  uses = "ScottBrenner/github-action@patch-3"
  secrets = ["AWS_ACCESS_KEY_ID", "AWS_SECRET_ACCESS_KEY"]
  args = "deploy"
}
