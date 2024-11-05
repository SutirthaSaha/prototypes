#!/usr/bin/env bash
# build the docker image

kubectl config use-context dev

echo "================================================================================================="
echo "This script is only used during development to quickly deploy updates to a Canary/Dev cluster. "
echo "It is not called by the Jenkins. You should also not use it to patch or update a live cluster."
echo "================================================================================================="
echo ""

VERSION=v1
# adding "_dev" to the project to avoid to affect negatively the PROD docker repository
PROJECT=elasticsearch-flask
REPOSITORY=suti12

# causes the shell to exit if any subcommand or pipeline returns a non-zero status.
set -e

# set debug mode
#set -x


# build the new docker image
#
echo '>>> Building new image'
# Due to a bug in Docker we need to analyse the log to find out if build passed (see https://github.com/dotcloud/docker/issues/1875)
docker build --no-cache=true --rm -t $REPOSITORY/$PROJECT:$VERSION . --platform="linux/amd64"

echo '>>> Push new image'
docker push $REPOSITORY/$PROJECT:$VERSION
kubectl apply -f ./yaml
