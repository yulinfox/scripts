host='github.com'
hostName='github.com'
gitUser='testUser'
identityFile='testFile'

while getopts ":h:n:u:i:" opt
do
    case $opt in
        h)
        host=$OPTARG
        ;;
        n)
        hostName=$OPTARG
        ;;
        u)
        gitUser=$OPTARG
        ;;
        i)
        identityFile=$OPTARG
        ;;
        ?)
        echo "未知参数"
        exit 1;;
    esac
done

echo -e "#config文件通过host区分不同的托管库\nHost ${host}\nHostName ${hostName}\nUser ${gitUser}\nIdentityFile ${identityFile}"