#! /bin/bash
PROJECT_NAME="Dummy_Project-CI"

function usage {
    echo "usage: codebuild.sh buil|run|clean [options]"
    echo "build:"
    echo "  Build the project and corresponding report groups"
    echo "run:"
    echo "  Run the tests"
    echo "  Run Options:"
    echo "    -f FILE   Used to specify a buildspec override file. Defaults to buildspec.yml in the source directory."
    echo "clean:"
    echo "  Delete the Dummy_Project-CI build project"
    exit 1
}

while getopts "f:h" opt; do
    case $opt in        
        h  ) usage; exit;;
        \? ) echo "Unknown option: -$OPTARG" >&2; exit 1;;
        :  ) echo "Missing option argument for -$OPTARG" >&2; exit 1;;
        *  ) echo "Invalid option: -$OPTARG" >&2; exit 1;;
    esac    
done

shift $((OPTIND -1))

subcommand=$1; shift
case "$subcommand" in
  run)
    while getopts "f:h" opt; do
        case $opt in
            f  ) buildspec=$OPTARG;;
            h  ) usage; exit;;
            \? ) echo "Unknown option: -$OPTARG" >&2; exit 1;;
            :  ) echo "Missing option argument for -$OPTARG" >&2; exit 1;;
            *  ) echo "Invalid option: -$OPTARG" >&2; exit 1;;
        esac    
    done
    shift $((OPTIND -1))
    ;;
esac


function build {
    # Create Report Groups
    REPORT_ARN=$(aws codebuild create-report-group \
        --cli-input-json file://reportGroupReport.json \
        --query "reportGroup.{arn:arn}" \
        | grep "arn" | tr -d '"')
    REPORT_ARN=$(sed -E 's/arn:[[:space:]]?//g' <<< $REPORT_ARN)

    COVERAGE_ARN=$(aws codebuild create-report-group \
        --cli-input-json file://reportGroupCoverage.json \
        --query "reportGroup.{arn:arn}" \
        | grep "arn" | tr -d '"')
    COVERAGE_ARN=$(sed -E 's/arn:[[:space:]]?//g' <<< $COVERAGE_ARN)

    # Create Build Project
    PROJECT_ARN=$(aws codebuild create-project \
        --cli-input-json file://codebuild.json \
        --query "project.{arn:arn}" \
        | grep "arn" | tr -d '"')
    PROJECT_ARN=$(sed -E 's/arn:[[:space:]]?//g' <<< $PROJECT_ARN)

    echo "Report Groups:"
    echo "    - report  : $REPORT_ARN"
    echo "    - coverage: $COVERAGE_ARN"
    echo "Project:"
    echo "    - project : $PROJECT_ARN"
}

function run {
    if [ -n "$buildspec" ]; then
        aws codebuild start-build --project-name $PROJECT_NAME --buildspec-override $buildspec > /dev/null
        echo "Build has been started with custom buildspec file"
    else
        aws codebuild start-build --project-name $PROJECT_NAME > /dev/null
        echo "Build has been started"
    fi
}

function clean {    
    aws codebuild delete-project --name $PROJECT_NAME > /dev/null
    groups=$(aws codebuild list-report-groups --query "reportGroups" --output text)
    for g in $groups
    do        
        reports=$(aws codebuild list-reports-for-report-group \
                                --report-group-arn $g \
                                --query "reports"\
                                --output text)
        for r in $reports
        do
            aws codebuild delete-report --arn $r > /dev/null
        done
        aws codebuild delete-report-group --arn $g > /dev/null
    done
    echo "Build Project 'Dummy_Project-CI' and its reports have been deleted"
}

if [ $subcommand == "build" ]
then    
    build
elif [ $subcommand == "run" ]
then
    run
elif [ $subcommand == "clean" ]
then
    clean
else
    echo "Unknown command"
    exit 1
fi