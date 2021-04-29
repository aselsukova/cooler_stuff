#PBS -q bl2x220g7q
#PBS -l walltime=1:00:00
#PBS -l mem=14gb,ncpus=4

NORM=XX
DIS=XXX
# correlation.py hic2.cool[1] hic.cool[2] chr[3] start[4] end[5]

source ~/distributives/anaconda_ctale/bin/activate
cd /mnt/storage/home/aselsukova/aneuoloidies
python scc_table.py $NORM'.cool' $DIS'.cool' # chr8 133000000 134000000

module load anaconda/anaconda3
Rscript scc.r $NORM'-'$DIS