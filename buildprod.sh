for folder in mongodb_crud/CRUD/* ; do
    aws lambda publish-version --function-name $folder > res.json
    export VERSION=$(jq -r '.Version' res.json)
    aws lambda update-alias --function-name $folder --function-version $VERSION --name Prod
done