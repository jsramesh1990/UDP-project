#include <iostream>
#include <cstring>
#include <arpa/inet.h>
#include <unistd.h>

#define PORT 8080

int main() {
    int sockfd;
    char buffer[1024];
    struct sockaddr_in servaddr;

    sockfd = socket(AF_INET, SOCK_DGRAM, 0);

    servaddr.sin_family = AF_INET;
    servaddr.sin_port = htons(PORT);
    servaddr.sin_addr.s_addr = inet_addr("127.0.0.1");

    while (true) {
        std::string input;
        std::cout << "Enter: ";
        std::getline(std::cin, input);

        sendto(sockfd, input.c_str(), input.size(), 0,
               (struct sockaddr*)&servaddr, sizeof(servaddr));

        socklen_t len = sizeof(servaddr);
        memset(buffer, 0, sizeof(buffer));

        recvfrom(sockfd, buffer, sizeof(buffer), 0,
                 (struct sockaddr*)&servaddr, &len);

        std::cout << "Server Reply: " << buffer << std::endl;
    }

    return 0;
}
