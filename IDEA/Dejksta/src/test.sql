CREATE TABLE `students`
(
    `id`        INT          NOT NULL AUTO_INCREMENT UNIQUE,
    `firstName` VARCHAR(255) NOT NULL,
    `lastName`  VARCHAR(255) NOT NULL,
    `classId`   INT          NOT NULL,
    PRIMARY KEY (`id`),
    FOREIGN KEY (`classId`) REFERENCES `classes` (`id`)
);

CREATE TABLE `transactions`
(
    `id`          INT          NOT NULL AUTO_INCREMENT,
    `description` VARCHAR(255) NOT NULL,
    `amount`      DECIMAL      NOT NULL,
    PRIMARY KEY (`id`)
);

CREATE TABLE `transaction_students`
(
    `transactionId` INT     NOT NULL,
    `studentId`     INT     NOT NULL,
    `isPaid`        BOOLEAN NOT NULL DEFAULT false,
    PRIMARY KEY (`transactionId`, `studentId`),
    FOREIGN KEY (`transactionId`) REFERENCES `transactions` (`id`),
    FOREIGN KEY (`studentId`) REFERENCES `students` (`id`)
);

CREATE TABLE `classes`
(
    `id`   INT          NOT NULL AUTO_INCREMENT,
    `name` VARCHAR(255) NOT NULL,
    PRIMARY KEY (`id`)
);