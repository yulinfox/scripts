host='github.com'
hostName='github.com'
user='testUser'
identityFile='testFile'

while getopts ":host:hostName:user:identityFile" opt
do
  case $opt in
    host)
    host=$OPTARG
    ;;
    hostName)
    hostName=$OPTARG
    ;;
    user)
    user=$OPTARG
    ;;
    identityFile)
    user=$OPTARG
    ;;
  esac
done

echo -e "#config文件通过host区分不同的托管库\nHost ${host}\nHostName ${hostName}\nUser ${user}\nIdentityFile ${identityFile}"