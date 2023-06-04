#set -x
SCRIPTPATH=$(cd "$(dirname "$0")"; pwd -P)

cd "$SCRIPTPATH"

SUDO=sudo

#gcc and libssl-dev is needed so that python components get installed
for p in python3-pip python3-venv gcc
do
	$SUDO apt-get update
	$SUDO env DEBIAN_FRONTEND=noninteractive $aptget -y install "$p"
done


python3 -m venv ../shop_finder_venv
source ../shop_finder_venv/bin/activate

python3 -m pip show djangorestframework &>/dev/null

if (( $? != 0 ))
then
	python3 -m pip install --upgrade pip
	python3 -m pip install wheel
	python3 -m pip install anyio Django==3.2 djangorestframework
fi
