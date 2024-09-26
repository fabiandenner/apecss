######### Parameters ################################################################################################################################

ncores=12
nbubbles=250

pressure=-3.0e4

######### No interaction computations ###############################################################################################################

cd NI/build
./compile.sh
cd ..

./build/sphericalclustertensionwave_apecss -options run.apecss -amp $pressure -tend 15.0e-6
python3 gather_results.py

cd ..

echo ""
echo "No interaction test cases passed"
echo ""

######### Incompressible computations ###############################################################################################################

cd IC/build
./compile.sh
cd ..

./build/sphericalclustertensionwave_apecss -options run.apecss -amp $pressure -tend 15.0e-6
python3 gather_results.py

cd ..

echo ""
echo "Incompressible test cases passed"
echo ""

######### Quasi acoustic computations ###############################################################################################################

cd QA/build
./compile.sh
cd ..

mpiexec -n $ncores ./build/sphericalclustertensionwave_apecss -options run.apecss -amp $pressure -tend 25.0e-06
python3 gather_results.py

cd ..

echo ""
echo "Quasi acoustic test cases passed"
echo ""

######### Plot results ##############################################################################################################################

python3 plot_results.py

######### Cleaning ##################################################################################################################################

cd NI
rm -rf "tension_results.txt" "bubble_loc.txt"
for ((c=0; c<$nbubbles; c++))
do
    rm -rf Bubble_$c
done
cd ..

cd IC
rm -rf "tension_results.txt" "bubble_loc.txt"
for ((c=0; c<$nbubbles; c++))
do
    rm -rf Bubble_$c
done
cd ..

cd QA
rm -rf "bubble_loc.txt"
for ((c=0; c<$ncores; c++))
do
    rm -rf tension_results_$c.txt
done
for ((c=0; c<$nbubbles; c++))
do
    rm -rf Bubble_$c
done
cd ..

echo ""
echo "Cleaning completed"
echo ""