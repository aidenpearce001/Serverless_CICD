for folder in mongodb_crud/CRUD/* ; do
    func_name=$(echo $folder | cut -d "/" -f 3)
    aws lambda publish-version --function-name $func_name > res.json
    export VERSION=$(jq -r '.Version' res.json)
    aws lambda update-alias --function-name $func_name --function-version $VERSION --name Prod
done