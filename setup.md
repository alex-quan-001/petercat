Setup on orbstack-Ubuntu

 - Download the setup script:

curl -fsSL https://deb.nodesource.com/setup_23.x -o nodesource_setup.sh

 - Run the setup script with sudo:

sudo -E bash nodesource_setup.sh

 - Install Node.js:

sudo apt-get install -y nodejs

 - Verify the installation:

node -v

 - Install via npm

npm install --global yarn

 - Verify the installation:

yarn --version

 - Install git and verify

sudo apt-get install git

git -v

 - Install PeterCat

git clone https://github.com/petercat-ai/petercat.git

cd petrcat

sudo apt install python3.12-venv

yarn run bootstrap

cp client/.env.local.example client/.env

cp server/.env.local.example server/.env

 - Install supbase
   

cd ..

git clone --depth 1 https://github.com/supabase/supabase


# 安装依赖工具
sudo apt-get update
sudo apt-get install apt-transport-https ca-certificates curl gnupg software-properties-common

# 添加 Docker 官方 GPG 密钥（国内用户可选阿里云源）
curl -fsSL https://mirrors.aliyun.com/docker-ce/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg

# 添加 Docker APT 源
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://mirrors.aliyun.com/docker-ce/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

# 安装 Docker
sudo apt update
sudo apt install docker-ce docker-ce-cli containerd.io

sudo systemctl restart docker

cd ~/supabase/docker/

docker compose pull

sudo docker compose up -d

mkdir -p  ~/.aws/

vim ~/.aws/config


[default]
region = us-west-2

cd ~/petercat/

yarn run server:local


wget https://github.com/supabase/cli/releases/download/v2.15.9/supabase_2.15.9_linux_arm64.deb

sudo dpkg -i ./supabase_2.15.9_linux_arm64.deb


