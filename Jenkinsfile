def label = "worker-${UUID.randomUUID().toString()}"

podTemplate(label: label, containers: [
  containerTemplate(name: 'docker', image: 'docker', command: 'cat', ttyEnabled: true),
  containerTemplate(name: 'kubectl', image: 'lachlanevenson/k8s-kubectl', command: 'cat', ttyEnabled: true),
  containerTemplate(name: 'helm', image: 'lachlanevenson/k8s-helm', command: 'cat', ttyEnabled: true)
],
volumes: [
  hostPathVolume(mountPath: '/var/run/docker.sock', hostPath: '/var/run/docker.sock')
]) {
  node(label) {
    stage('Create Docker images') {
      container('docker') {
        checkout scm: scm
        sh "docker images"
      }
    }
    stage('Run kubectl') {
      container('kubectl') {
        withCredentials([file(credentialsId: 'kube-config', variable: 'KUBECONFIG')]) {
            sh "kubectl get pods"
        }
      }
    }
    stage('Run helm') {
      container('helm') {
        withCredentials([file(credentialsId: 'kube-config', variable: 'KUBECONFIG')]) {
            sh "helm list"
        }
      }
    }
  }
}