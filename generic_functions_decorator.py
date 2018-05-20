""" Decorator that check accepted types """

def accepts(*types):
    def check_accepts(f):
        assert len(types) == f.func_code.co_argcount
        def new_f(*args, **kwds):
            for (a, t) in zip(args, types):
                assert isinstance(a, t), \
                       "arg %r does not match %s" % (a,t)
            return f(*args, **kwds)
        new_f.func_name = f.func_name
        return new_f
    return check_accepts

""" Decorator that check returned types """

def returns(rtype):
    def check_returns(f):
        def new_f(*args, **kwds):
            result = f(*args, **kwds)
            assert isinstance(result, rtype), \
                   "return value %r does not match %s" % (result,rtype)
            return result
        new_f.func_name = f.func_name
        return new_f
    return check_returns


""" Decorator that check time of a function """

def timecontrol(maxtime):
    def check_time(f):
        """ Check if time of execution > maxtime. """
        def new_f(*args, **kwargs):
            start = time.time()
            result = f(*args, **kwargs)
            stop = time.time()
            finaltime = stop-start
            if (finaltime > maxtime):
                print("Alert! The function is slow! ({0:.2f} secs)".format(finaltime))
            return result
        return new_f
    
    return check_time