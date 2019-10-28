n=0
until [ $n -ge 10 ] ; do
   python run.py -r
   n=$[$n+1]
   sleep 60
done
