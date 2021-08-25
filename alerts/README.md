# Setting up Cronjobs for various alerts

## RHOSP Daily Standup alert

1. create webhook url secret

```bash
kubectl create secret generic coreos-tektondev-webhook --from-literal=url=<webhook url to coreos slack #tekton-dev>
```

1. create cronjob

```bash
kubectl apply -f cronjob-rhosp-daily-standup-notification.yaml
```

1. (optional) test cronJob

```bash
kubectl create job --from=cronjob/rhosp-standup-notify test-job-1
```
