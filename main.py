import argparse
from modules.connect import connect_to_cluster
from modules.deploy import deploy_manifest

def main():
    parser = argparse.ArgumentParser(description="Kubernetes Management CLI")
    subparsers = parser.add_subparsers(dest="command")

    # Connect and install tools
    cluster_connect = subparsers.add_parser("connect", help="Connect to Kubernetes cluster and verify")
    cluster_connect.add_argument("--kubeconfig", default="~/.kube/config", help="Config file with required credentials for connecting to the cluster" )

    # Create deployment
    create_parser = subparsers.add_parser("deploy", help="Create a deployment")
    create_parser.add_argument("--config", required=True, help="Path to deployment config YAML")  
    create_parser.add_argument("--name", required=True, help="Deployment name") 

    # Health check
    health_parser = subparsers.add_parser("health", help="Check deployment health")
    health_parser.add_argument("--name", required=True, help="Deployment name")
    health_parser.add_argument("--namespace", default="default")

    args = parser.parse_args()

    if args.command == "connect":
        connect_to_cluster(args.kubeconfig)

    elif args.command == "deploy":
        deploy_manifest(args.config, args.name)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
