def b2():
    import scipy.stats

    x = [183, 168, 177, 170, 175, 177, 178, 166, 174, 178]

    mu = 175
    sigma = 5

    world_height_mean = 165
    world_height_standard_deviation = 7

    prior = scipy.stats.norm.pdf(x[0], world_height_mean, world_height_standard_deviation * 2)

    likelihoods = scipy.stats.norm.pdf(x, mu, sigma)

    posterior = prior * likelihoods[0]
    print(prior.round(2))
    print(likelihoods.round(2))
    print(posterior.round(2))

def b3():
    import scipy.stats

    x = [183, 168, 177, 170, 175, 177, 178, 166, 174, 178]

    mu = 175
    sigma = 5

    world_height_mean = 165
    world_height_standard_deviation = 7

    prior = scipy.stats.norm.pdf(x[0], world_height_mean, world_height_standard_deviation * 2)

    likelihoods = scipy.stats.norm.pdf(x, mu, sigma)

    posterior = prior
    for likelihood in likelihoods:
        posterior = posterior * likelihood

    print(posterior)


def b4():
    import scipy.stats

    x = [183, 168, 177, 170, 175, 177, 178, 166, 174, 178]

    mu = 175
    sigma = 5

    world_height_mean = 165
    world_height_standard_deviation = 7

    prior = scipy.stats.norm.pdf(x[0], world_height_mean, world_height_standard_deviation * 2)

    x=prior * scipy.stats.norm.pdf(x, mu, sigma).prod()
    print(x)


b2()
print('\n\n\n')    
b3()
b4()

