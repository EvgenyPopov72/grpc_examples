package main

import (
	"context"
	"google.golang.org/grpc"
	"google.golang.org/grpc/credentials/insecure"
	"log"
	"time"

	pb "github.com/EvgenyPopov72/grpc-services/grpc_go/grpc_hub"
)

func main() {
	conn, err := grpc.Dial("localhost:50051", grpc.WithTransportCredentials(insecure.NewCredentials()))
	if err != nil {
		log.Fatalf("did not connect: %v", err)
	}
	defer conn.Close()
	client := pb.NewSimpleServiceClient(conn)

	for {
		ctx, cancel := context.WithTimeout(context.Background(), time.Second)
		defer cancel()

		response, err := client.Ping(ctx, &pb.PingMessage{Body: "Ping"})
		if err != nil {
			log.Fatalf("An error occured: %v", err)
		}
		log.Printf("Got messege: %s", response.Body)
		time.Sleep(time.Second)
	}
}
