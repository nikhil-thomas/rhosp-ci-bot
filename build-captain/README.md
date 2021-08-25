# Build Captain Bot

## Set up

1. Generate build captain roster

    1. Clone tektoncd/plumbing
        ```bash
   
        ```
    2. Generate build captain roster
        ```bash
         go run ./main.go -start-date 2021-08-25 -days $((18 * 7)) -start-name nikhilthomas@UG80L4CJ0 -names \
         name@slack-user-id,\
         name@slack-user-id,\
         name@slack-user-id,\
         name@slack-user-id
         > rhosp-rotation.csv
        ```
    3. Create configmap with build captain roster
       ```bash
       kubectl create configmap rotation-roster --from-file=rotation-roster.csv=rhosp-rotation.csv 
       ```
    
2. Add Tasks and Pipelines
   ```bash
    kubectl apply -f task-set-captain.yaml
    kubectl apply -f pipeline-notify-buildcaptain.yaml
    tkn hub install task send-to-webhook-slack
   ```
3. Create webhook-url secret
   ```bash
    kubectl create secret generic coreos-tektondev-webhook --from-literal=url=<webhook url to coreos slack #tekton-pipeline-ci>
   ```
   
5. Create rbac for cronjob
   ```bash
   kubectl apply -f clusterrole-tekton-edit.yaml
   kubectl apply -f rolebinding-tekton-edit.yaml
   ```
   
6. Create CronJob
   ```bash
   kubectl apply -f cronjob-rhosp-build-captain-notification.yaml
   ```
   
7. (optional) test cronjob
    ```bash
    kubectl create job --from=cronjob/trigger-build-captain-notify test-job-1
    ```
