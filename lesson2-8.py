#task 1
from pylab import plot, show, title, xlabel, ylabel, legend, savefig

temp_brno=[-2.1,-0.1, 3.9, 9.2, 14.2, 17.3, 18.9, 18.6, 14.4, 9.1, 3.5, -0.6]
temp_hydbad=[17.9, 21.1, 26.5, 30.6, 33.9, 34.3, 33.1, 31.9, 31.2, 29.6, 24.5, 19.3]
temp_toronto=[-1.6, 1.3, 7.5, 13.9, 18.7, 23.4, 26.5, 25.5, 20.9, 14.8, 7.6, 1]
temp_joen=[-10.7, -10.6, -5.2, 1.2, 8.2, 14.2, 16.4, 14.3, 8.8, 3.2, -2.7, -7.8]

months = range(1,13)
plot(months, temp_brno,months, temp_hydbad, months,temp_toronto, months, temp_joen)
title('Average monthly temperatures')
xlabel('Month')
ylabel('Temperature')
legend(['Brno', 'Hyderabad', 'Toronto', 'Joensuu'])
savefig('temp_graph.png')
show()
