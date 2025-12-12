#include "mainwindow.h"
#include "ui_mainwindow.h"
#include <QUdpSocket>

QUdpSocket udp;

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
{
    ui->setupUi(this);
}

MainWindow::~MainWindow() {
    delete ui;
}

void MainWindow::on_sendButton_clicked() {
    QString msg = ui->inputBox->text();

    udp.writeDatagram(msg.toUtf8(),
                      QHostAddress("127.0.0.1"),
                      8080);

    ui->outputBox->append("Sent: " + msg);
}

