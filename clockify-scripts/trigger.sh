#!/bin/bash



CMD=${CMD:-clockify-cli}
PROJECT_ID=${PROJECT_ID:-67c9f957f9ec225c223237a6}
CLIENT_ID=${CLIENT_ID:-67c9f9424ca1cb7a1b2395c0}
TASK_ID=${TASK_ID:-67c9f958de816e1eb4c2e2e9}
TAG_ID=${TAG_ID:-5ee226022890403cbb0f488d}
NOW=${NOW:-$(date +"%Y-%m-%d %T")}
DESC=${DESC:-"testing mk815 at $NOW"}

notify-send "Clockify Trigger" "Closing current time entry"
$CMD out

notify-send "Clockify Trigger" "Starting new time entry: $DESC"
$CMD in --interactive=0 -c "$CLIENT_ID" -p "$PROJECT_ID" -d "$DESC" --task "$TASK_ID" --tag "$TAG_ID"
