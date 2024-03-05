#!/usr/bin/env sh

result=$(curl --request POST --header "PRIVATE-TOKEN: ${VRS_OPS_ACCESS_TOKEN}" "${CI_API_V4_URL}/projects/${VRS_OPS_PROJECT_ID}/pipeline_schedules/${VRS_OPS_DEVELOP_DEMO_SCHEDULE_ID}/play")
