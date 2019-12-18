import os, tfutil, misc, argparse, torch
from proggan import from_tf_parameters

def main():
    os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 
    parser = argparse.ArgumentParser(
            description='converter to create pytorch models')
    #parser.add_argument('--id', type=int, required=True,
    #        help='number of model to convert')
    parser.add_argument('--id', type=str, required=True, help='number of model to convert')
    parser.add_argument('--outdir', default=None)
    args = parser.parse_args()

    # Configuration
    snapshot = None  # Default, implies last snapshot

    # Get parameters from checkpoint
    tfutil.init_tf()
    directory = misc.locate_result_subdir(args.id)
    print('Loading snapshot from %s' % directory)
    G, D, Gs = misc.load_network_pkl(args.id, snapshot)
    print(G)
    print(D)
    print(Gs)

    # import pdb; pdb.set_trace()


    # model = from_tf_parameters(Gs.variables)
    model = from_tf_parameters(Gs.vars)
    if args.outdir is None:
        args.outdir = directory
    filename = os.path.join(args.outdir, 'generator.pth')
    print('Saving pytorch model as %s' % filename)
    torch.save(model.state_dict(), filename)

if __name__ == '__main__':
    main()
