# CS544 Homework 4
# Yuxiao Wu
# 10/31/2021
options(scipen = 999, digits = 2)
# Part 1 Binomial distribution
# a)
n = 5; p = 0.4;
pmf = dbinom(0:n, size = n, prob = p)
pmf

plot(0:n, pmf, type = "h", xaxt = "n",
     main = "", xlab = "x", ylab = "PMF")
points(0:n, pmf, pch = 16)   
axis(side = 1, at = 0:n, labels = TRUE)
abline(h = 0, col="red")

cdf = c(0, cumsum(pmf))
cdf

cdfplot = stepfun(0:n, cdf)
plot(cdfplot, verticals = FALSE, pch = 16,
     main = "", xlab = "x", ylab = "CDF")

# b)
# P(X = 2)
dbinom(2, size = n, prob = p)

# c)
# P(X >= 2)
sum(dbinom(2:n, size = n, prob = p))

# d)
r = rbinom(1000, size= n, prob= p)
plot(table(r))


# Part 2 Negative Binomial distribution
# a)
r <- 3; p <- 0.6

pmf <- dnbinom(0:10, size = r, prob = p)
pmf

#Plot PMF
plot(0:10,pmf,type="h",
     xlab="x",ylab="PMF", ylim = c(0, 0.3))
abline(h=0, col="red")

cdf <- c(0, cumsum(pmf))
cdf

#Plot CDF
cdfplot <- stepfun(0:10, cdf)
plot(cdfplot, verticals = FALSE, pch = 16,
     main = "", xlab = "x", ylab = "CDF")

# b)
# P(X = 4)
dnbinom(4, size = r, prob = p)

# c)
# P(X <= 4)
pnbinom(4, size = r, prob = p)

# d)
r = rnbinom(1000, size = r, prob = p)
plot(table(r))


# Part 3 Hypergeometric distribution
# a)
M <- 60; N <- 40; K <- 20
pmf <- dhyper(0:K, m = M, n = N, k = K)
pmf
# Plot PMF
plot(0:20,pmf,type="h",
     xlab="x",ylab="PMF", ylim = c(0, 0.25))
abline(h=0, col="red")
# Plot CDF
cdf <- c(0, cumsum(pmf))
cdfplot <- stepfun(0:K, cdf)
plot(cdfplot, verticals = FALSE, pch = 16,
     main = "", xlab = "x", ylab = "CDF")

# b)
# P(X = 10)
dhyper(10, m = M, n = N, k = K)

# c)
# P(X >= 10)
phyper(10, m = M, n = N, k = K, lower.tail = FALSE)

# d)
r = rhyper(1000, m = M, n = N, k = K)
plot(table(r))

# Part 4 Poisson distribution
# a)
dpois(8, lambda=10)

# b)
ppois(8, lambda=10)

# c)
ppois(12, lambda=10) - ppois(6, lambda=10)

# d)
pmf <- dpois(0:20, lambda=10)
pmf
plot(0:20,pmf,type="h",
     xlab="x",ylab="PMF", ylim = c(0, 0.15))
abline(h=0, col="red")

# e)
r = rpois(50, lambda = 10)
plot(table(r))
boxplot(r, horizontal = TRUE)
fivenum(r)
# in most days, 8-12 students will attend the office
# hour.

# Part 5 Normal distribution
# a)
x <- seq(70, 130)
mu <- 100; sigma <- 10
pdf = dnorm(x, mean = mu, sd = sigma)
plot(x, pdf, type="l", col="red", 
     xlim=c(70,130),
     main="Money Spent", xlab="Days", ylab="PDF")

# b)
pnorm(mu - 2*sigma, mean = mu, sd = sigma)

# c)
pnorm(mu - 1*sigma, mean = mu, sd = sigma) - 
        pnorm(mu - 2*sigma, mean = mu, sd = sigma)

# d)
# between 1 std
pnorm(mu + 1*sigma, mean = mu, sd = sigma) - 
        pnorm(mu - 1*sigma, mean = mu, sd = sigma)
# between 2 std
pnorm(mu + 2*sigma, mean = mu, sd = sigma) - 
        pnorm(mu - 2*sigma, mean = mu, sd = sigma)
# between 3 std
pnorm(mu + 3*sigma, mean = mu, sd = sigma) - 
        pnorm(mu - 3*sigma, mean = mu, sd = sigma)

# e)
lower <- qnorm(0.1, mean = mu, sd = sigma)
upper <- qnorm(0.9, mean = mu, sd = sigma)
paste("middle 80% of the money spent will fall Between", lower,"and",upper, "doallers")

# f)
qnorm(0.98, mean = mu, sd = sigma)
paste("The min you have to spend to get T-shirt is",qnorm(0.98, mean = mu, sd = sigma),"doallers")

# g)
r <- rnorm(10000, mean = mu, sd = sigma)
r <- round(r)
plot(table(r), type = 'h')

