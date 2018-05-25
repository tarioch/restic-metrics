podTemplate(label: "build-deploy-app", idleMinutes: 15, containers: [
  containerTemplate(name: 'packer', image: 'hashicorp/packer', command: 'cat', ttyEnabled: true),
  containerTemplate(name: 'docker', image: 'docker', command: 'cat', ttyEnabled: true),
  containerTemplate(name: 'kubectl', image: 'lachlanevenson/k8s-kubectl', command: 'cat', ttyEnabled: true),
  containerTemplate(name: 'helm', image: 'lachlanevenson/k8s-helm', command: 'cat', ttyEnabled: true)
],
volumes: [
  hostPathVolume(mountPath: '/var/run/docker.sock', hostPath: '/var/run/docker.sock')
]) {
  node(label) {
    stage('Create Docker images') {
      container('packer') {
        checkout scm: scm
          sh "packer version"
          sh "packer build template.json"
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
