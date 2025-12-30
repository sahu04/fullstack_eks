pipeline {
    agent any

    stages {

        stage('Checkout Code') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/sahu04/fullstack_ecs.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                cd backend
                npm install
                '''
            }
        }

        stage('Build App') {
            steps {
                sh '''
                cd backend
                npm run build || echo "No build step"
                '''
            }
        }

        stage('Deploy to EC2') {
            steps {
                sh '''
                rm -rf /var/www/fullstack/*
                cp -r * /var/www/fullstack/
                '''
            }
        }

        stage('Start Application') {
            steps {
                sh '''
                cd /var/www/fullstack/backend

                # stop old app if running
                pm2 stop all || true

                # start app
                pm2 start server.js --name backend-app
                pm2 save
                '''
            }
        }
    }
}
