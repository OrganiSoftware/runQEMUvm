import argparse
import os

class QEMU:
    def runQEMU(self):
        parser = argparse.ArgumentParser(description='get params needed to run QEMU vm')
        parser.add_argument('QEMU_path', help='path to QEMU executable')
        parser.add_argument('image_path', help='path to QEMU image')
        parser.add_argument('format', help='image format')
        parser.add_argument('accell', help='image accelerator')
        parser.add_argument('cores', help='num cores')
        parser.add_argument('mem', help='ram')
        args = parser.parse_args()
        os.system(str(args.QEMU_path)+" -accel accel="+str(args.accell)+" -m "+str(args.mem)+" -smp "+str(args.cores)
                  +" -boot order=d  -blockdev node-name=prot-node,driver=file,filename="+str(args.image_path)
                  +" -blockdev node-name=fmt-node,driver="+str(args.format)
                  +",file=prot-node  -device virtio-blk,drive=fmt-node,share-rw=on -device virtio-sound")

if __name__ == '__main__':
    runQEMU = QEMU()
    runQEMU.runQEMU()
