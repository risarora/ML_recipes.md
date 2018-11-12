IPython provides access to a wide array of functionality for this kind of timing and profiling of code. Here we'll discuss the following IPython magic commands:

* <code>%time</code>: Time the execution of a single statement
* <code>%timeit</code>: Time repeated execution of a single statement for more accuracy
* <code>%prun</code>: Run code with the profiler
* <code>%lprun</code>: Run code with the line-by-line profiler
* <code>%memit</code>: Measure the memory use of a single statement
* <code>%mprun</code>: Run code with the line-by-line memory profiler

The last four commands are not bundled with IPython–you'll need to get the <code>line_profiler</code> and <code>memory_profiler</code> extensions, which we will discuss in the following sections.
