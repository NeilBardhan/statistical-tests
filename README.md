# Statistical Tests of Significance

<p align = "center">
 +---------------------+ <br>
 |   Work in Progress  | <br>
 +---------------------+ <br>
</p>

This git repo implements some statistical tools that come in handy for performing tests of significance. Chiefly among them are -

* ANOVA
  * [One Way ANOVA](https://statistics.laerd.com/statistical-guides/one-way-anova-statistical-guide.php) Test
  * [Kruskal Wallis H](https://www.statisticshowto.datasciencecentral.com/kruskal-wallis/) Test - A non parametric alternative to the One Way ANOVA. [Non parametric](https://www.statisticshowto.datasciencecentral.com/parametric-and-non-parametric-data/) implies that the test doesn’t assume the data comes from a particular  distribution. The H test is used when the assumptions for ANOVA aren’t met (like the [assumption of normality](https://www.statisticshowto.datasciencecentral.com/assumption-of-normality-test/)). Also known as, **one-way ANOVA on ranks**, as the ranks of the data values are used in the test rather than the actual data points.
 * T-Tests
    * 2 Sample Independent T-Tests
    * Paired T-Tests
    * 1 Sample T-Test
 * Chi-Square
    * Chi-square goodness-of-fit
    * Chi-square categorical test
* [Wilcoxon-Mann-Whitney](https://thestatsgeek.com/2014/04/12/is-the-wilcoxon-mann-whitney-test-a-good-non-parametric-alternative-to-the-t-test/) test
* [Wilcoxon signed rank sum](http://www.statstutor.ac.uk/resources/uploaded/wilcoxonsignedranktest.pdf) test
