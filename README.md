# reddelete
Serverless Framework function that periodically deletes a user's Reddit comments below a defined threshold!

# Usage
1. Follow the Serverless Framework [AWS - Installation](https://serverless.com/framework/docs/providers/aws/guide/installation/) guide to setup Serverless Framework and AWS credentials in your development environment.
2. Set `functions.reddelete.events.schedule` in `serverless.yml` based on the [Schedule Expressions for Rules](https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/ScheduledEvents.html) guide _(default is every six hours)_
3. Set `functions.reddelete.environment` in `serverless.yml` as follows:
    * `REDDIT_CLIENT_ID`: [create an app on Reddit](https://ssl.reddit.com/prefs/apps/)
    * `REDDIT_CLIENT_SECRET`: from Reddit app created above
    * `REDDIT_USERNAME`: Reddit username
    * `REDDIT_PASSWORD`: Reddit password
    * `DELETE_THRESHOLD`: Comments with score below this are deleted _(default is 0)_
    
    _Suggested method for seting these values: [Reference Variables using the SSM Parameter Store](https://serverless.com/framework/docs/providers/aws/guide/variables/#reference-variables-using-the-ssm-parameter-store)_
4. `serverless deploy`
5. Done!

---
_This function is based on [AWS Python Scheduled Cron Example](https://github.com/serverless/examples/tree/master/aws-python-scheduled-cron)_