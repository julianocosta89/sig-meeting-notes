SIG: eBPF instrumentation
Date: 2025-07-30
Duration: 59 minutes
Zoom Recording URL: https://zoom.us/rec/share/jaDitQqJB_9dctzMzkTRPSfbZfzQoaJXRUW0nWyA7bR2kKS-BgaBqj5R7XnyhdUE.5w_LRuwt-ffuKUdN
============================================================

## Zoom Recording Transcript

**Stephen Lang** 00:44 Hi.
**Mattia Meleleo** 00:50 Hello!
**Rafael Roquetto** 00:52 Hi! There!
**Tyler Yahn** 02:12 Hey? Everyone.
how y'all doing?
**Rafael Roquetto** 02:21 Waking up.
**Tyler Yahn** 02:24 Yeah.
yes, we can probably get started here in just a second. I've added some agenda items that we had posted for last time. So, Nicola and Nimrod, if that's okay, please take a look at those. Otherwise, if you have things you want to talk about.
we go ahead and add them to the agenda as well, and we can get started here in just a second.
Awesome well, welcome, everyone, if you haven't yet also added name to the attendees list. Please go ahead and do that as well.
1st up. I had copied over the item, Nicola, you wanted to walk through distributed tracing and decision making. We had talked about this last time, just doing a little bit of a code review for this. Is this still something you're looking to do.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 03:41 Yeah, I'll do it. Yeah, that's super open. Yup.
Okay, yeah. I'm guessing.
**Tyler Yahn** 03:47 You'll probably want to share your screen. Then.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 03:50 Yeah, I'll share share my screen. Yeah, I don't have a presentation made. Although we do have some slides in the past how we we do this. So maybe let me see if I can find something.
If you guys want to just dive into code, we're just happy to do that as well. Whatever is preferable. I could.
**Tyler Yahn** 04:13 Yeah, I don't have too much of a preference. I'm interested in seeing both yours and Nimrod's demo as well. Yeah.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 04:21 Okay, alright. So I'll just dive into code because I think a presentation I may have like,
I'm trying to think I.
So maybe the one that we use with Mike on how we did this in the past. I wonder if that could
work? Well, just as an intro.
okay, yeah, I'm not prepared. Therefore, I'm just gonna go with the code.
**Tyler Yahn** 04:50 Oh, sorry!
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 04:52 Yeah.
Okay.
**Tyler Yahn** 05:03 Yeah, I mean, like, if you had a pre your previous presentation as well that I mean, I'm not.
I have no idea. But I'm guessing something would be.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 05:11 Yeah, I think we have a previous presentation on this topic.
Oh, I don't know what I did. There.
You guys still see my screen? Yeah.
**Tyler Yahn** 05:26 Yep.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 05:27 Okay, so let me close out the stuff.
Okay,
I'm gonna zoom in a bit. Just kind of to give an overview of how we do context propagation. So this is in the docs as well explained a little bit
But essentially, there was the traditional context distributed, tracing support done for go, which we
did, similar to something that go audience limitation does
slightly different approach. But at the end of the day. I think Htp is now the same grpc, slightly different. Still.
So we call that sort of the legacy contest distribute tracing support for injecting the the headers.
The reason why is that it relies on the Bpf probe right user helper which
is being sort of locked down and progressively over this couple of years that I've been working at least on this has been more and more locked down.
One recent sort of discovery you had is that? If you use what is it called elastic Kubernetes service aks
on Amazon right now in the last. I don't know how many revisions
the default. Kernel images you get are all locked down so you can't use the helper, but we still support it because it may.
I mean, we may need it right? So if it's on lock kernel, this kind of works really well for go so typically. So I'll start with the go tracer first, st how that happens for go programs.
And then I'll go into how we handle it for every other programming language? Where because go is typically done through you pros?
Does it make sense any questions? So far?
Nope.
**Tyler Yahn** 07:37 Sounds good.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 07:39 Okay, alright. So let me zoom this a little bit.
So typically on a server request when we
have an incoming server request. We want to read the transparent header that's passed in through. The the headers. So I'll
start with Http.
It's it's an easier one to to deal with
And so, typically for Http, we we have
the headers coming in on a I believe a map.
If I'm not mistaken, so serve Http,
We try to find out. The decoded header trace parents. This information should already be set up for us when we get into the serve Http probe.
The reason why we look up for ongoing this server request to try to find if we have decoded
server. Transparent information is because, go recently, in version 1, 24 changed the map implementation. So we haven't actually implemented map reading yet for go.
So we rely on the goes
parsing of the headers one by one. It's not efficient. But this is what we have. So technically, when the incoming request goes to the code in the go program, we set a U probe
So if I go to the go tracer
program we set a U probe that. Reads the request. Header on this server. No, this is Json, Rpc, sorry. Let me see
text program.
I need to see where my probe is, is it? Put it at the end or in the start?
That's not it.
Okay?
So we're gonna have to find it.
Yeah, this thing process headers, I believe.
So we can look up where this is being set. The ongoing server requests
so this programs every time.
Let's see where this is. So http.
yeah, so handle tracer and header.
Oh.
so this read continuous license. Apparently. That's the one that that pro we've put in, and this gets called every time headers are being parsed by various protocols.
So we kind of parse in the header set up this information
in a map. And then on the server handler, we read that information essentially.
So, this is purely the incoming path.
The outgoing path. So when we have to propagate the header outwards to an outgoing request. This is now involving the
the client request.
So this is where we write the outgoing cater information. So the outgoing header information it's easiest to find using searching for
Vpf, probe.
I can't see what I'm searching on
so right user. So this is what it looks like. Typically when we
we tap into this right, subset and it
and a specific information in place when the buffer is already pre-allocated for us in the.
So when the when the buffer is
at some point in the U in the go program
outgoing request, they've allocated the buffer and the written part. They say the get slash part of the request, we find the appropriate location, and then we inject this transparent using. This is one approach that we take. By looking at this right subset header, and then we find the place where we write in the buffer. We write the bytes adjust the the buffer
N. Field, which is how many bytes have been written, and then the rest of the headers come in that the goal program will typically inject
so similar thing happens for grpc, it's just a lot more complicated because Grpc's protocol is a bit more complex. But if we jump into Grpc and search for right user. Oh, actually,
you're gonna see? It looks exactly the same. It's a different
helper. The Grpc is slightly different, because
we cannot write the headers as
at the beginning, because Grpc uses certain kind of like protocol headers. So if you write in the beginning you break the protocol, so we need to go last. We are a Grpc. For Http. Doesn't matter. All headers are equal, but Grpc. Requires that the
there's certain headers that are prefixed with a colon, I think. That's like the method the
protocol like. And all all these other things that they're kind of system or default. Headers need to go 1st in the protocol. If they're not, then it doesn't parse well. But similar thing happens how we write this app.
Okay, so this is the the legacy support that may not work depending on. If you have a lock kernel. So if you do have lock kernel, or say, for example, you're running eks with the latest or the previous, or the 2 previous versions. You will not be able to use this approach, and ob will print this warning saying, you're running a lock kernel, or you haven't given a sysadmin permission, and we're unable to do this.
So what happens in in this scenario is, if you will look at our
go generate command lines for when we kind of try to do this.
That's why we have a Tp version and a non Tp version.
So these differ by the fact that one of them is, has this flag that says no header propagation. So technically, Obi will try to load the version
that has this pro bride user.
And if you can't and guess an error message saying that I can't because this helper is not found, or this helper. Recently there was a new kernel that changed the message that says this helper cannot be used from this function.
Then we load a different program that's precompiled with this code taken out
essentially. And then we attempt to load that one, and if that one fails, then we fail the tracer.
alright. So then how does the work? How does the the next? The new contrast? Tracer. Sorry
outgoing trace in parent injection and parsing of header work. In the
the second approach we use this a second approach. We've only implement for Htp grpc, we just don't.
We know how to do it? It just hasn't been like we haven't had the time to do it yet.
But essentially if we so the second approach relies on these socket programs.
So and we use 2 of these socket programs that we attach in
in the generic tracer. And those socket programs get attached.
For both go and generic programs so they will get loaded, no matter which tracer you enable by or whichever program you're instrumenting. Even if you instrument just go programs. We will still do it
alright. So they the the socket programs. They're in this
sort of like thing called deep injector, the trace parent injector.
So how does this work?
it's a little bit different. I'll talk about how. Let's let's 1st talk about how we read the incoming headers
on a incoming request. This is sort of relies on a newer kernel support
could be done better, and we're looking for help if anybody wants to tackle this.
But essentially, let me see if I can find it.
There's so many tries calling trace common, maybe.
Yeah.
So so the trace parent ingestion. There, there is one
one major function. I'm just trying to find it. This will be in the protocol. I think it should be an Http
I assume, because it's only implemented for Htp,
so there's this massive function which is called Http get or create trace info.
So this function attempts to find a trace information. For for example, a server request.
right? So typically comes through here
and wants to look at the incoming header buffers to try to find
the information. What's encoded in headers? However, you can see some other stuff happening here, and I'll get into details about what this is in a little bit. But the typical
way we kind of try to find if this transparent parsing is enabled, it must be specifically enabled. It's not on by default.
We kind of look for
transparent in the headers, by using Dpf loop.
So this this is why this is only supported
on newer kernels where Bpf loop is supported because we don't know how big the headers are
technically, we could write a simpler function. That kind of iterates over some number of characters, but this was
not implemented, so
it will use Bpf loop loop through the headers, try to find transparent, match it, extract the information.
and then stored in a map to be used later on as a source of truth, what should be the incoming request?
So that typically is how we read the incoming headers. And this is how traces start. If a header information is passed to ob through another SDK, or to an Http request, or something like that.
The outgoing part goes through this call program called Tp injector.
So this deep injector.
does a little bit of extra work to detect the protocol, because it's it's a separate program. That kind of runs
on a sort of independently from everything else. It had to be done that way. But
the key to that are 2 programs. One is this sk message program which
people use to manipulate the protocol before it reaches that the Tcp IP stack. Essentially
so. It's sort of an intermediate program, that
kind of like. It's after your
construction of the Tcp packet. Not everything is created. So, for example, you don't have access to the IP information here. None of that is available.
But it's not fully created a packet yet, so there's no IP section
but we do know what the IP addresses are, and they're encoded in this sk message, Md, data structure.
So we extract the connection information there and then we try to look up data set up by the go programs or the K. Probes to figure out
which request was this, do we have transparent information that we want to push down the wire?
Does it make sense? So far. Am I going too fast? Any feedback.
**Tyler Yahn** 21:28 So this is for the outgoing communication.
That's right
to set that. Yeah. And so where? Where is the information from the Http or our other place gonna come from? Is it? Just sit in the map or.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 21:40 Yes, it's sitting in this map that are shared. So, for example, we can see how, since I talk about the the goal
we can. We can check to see how this go is passing us the information. So we we kind of like the 2 different maps, go sets of one map because it has certain level of information.
And then for the rest, we we write it slightly differently, just because our goal is
telling us what it does. Because, say, for example, the go was able to use the the traditional way of context propagation. We don't need to do it twice. Essentially, we don't want to write the header twice, so go sets up this information, or it doesn't set up in one way, and the Cape probes they don't have another way. So they just set up the information through a different map.
And if we go.
**Tyler Yahn** 22:35 How? How are we tracking? What? What go process sent this.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 22:40 So that's a good question. Yeah.
So in ob, we, we have this concept of this Tp info, pity. So every information that we pass around gets encoded in this data structure which contains the trace parent, but also context about which process Id are is involved or thread whatever.
And
this information. Then everything's matched by the pit. Because this concept of this sock message program has no knowledge of the process. Ids, it needs to be told it just sees packets right?
So so we
we pull this information based on this E key. So if you look at the go, Nat, htp.
we can probably find this by looking at. This e key.
**Tyler Yahn** 23:41 Okay, so it's it's specifically a port and
yes. So we use a port just for destination port.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 23:49 We're assuming that in this mode we're running in a host mode. So we should see that being unique, I know there was a question before, and I'm not sure but technically, we set up this outgoing trace map.
and you can see that if we successfully wrote the information, the traditional way we go in, find the outgoing client connection by the Go routine. If we find the info there from the info, we construct the this key with the destination source port, and we remove the outgoing trace map, saying that we wrote the trace parent using the traditional way. We don't want the Tp injector to do it yet one more time.
but otherwise this outgoing trace map is set up.
In, I guess persistent connection round trip before the connection is being sent.
we have access to the connection information from where we're going to extract the ports. Because when you think about it, the sock message programs. They don't
have a concept of a go go routine or anything of that kind.
They, the only thing they have is the process Id, and they have the port information. So for this to work.
We have to be really meticulous about extracting the connection information from the go program.
So there's various places where we can pull this information from. On an outgoing client request we put a U probe and this persistent connection round trip
and the connection information and then is available there.
So you can see, we pull this concom pointer, we read, if it's a Tls state, then we need to unwrap that because Tls connection, information is different structure.
So we extract it. If it's Tls
and then we pull out information about source destination IP source ports destination port.
which is then used for this key
that we set up this trace map.
So if the kernel was locked, we couldn't actually propagate using the standard or the traditional injection approach. We set up this information here, and then the Tp injector looks it up. It has the connection info, and the process. Id
makes a key.
pulls the information to see if this key is actually tracked for a certain pit. We say, if we should handle as a goal request, do it, and so on.
The
now, when it's a go program, we don't need to check the protocol to know is this Htp. Or something else. This is why there's like, go approach and non-go approach. In go. We set this up from you probes. So we know exactly that we're doing Http requests. So this information about
what this thing is would never be anything weird.
Now, when we're running K probes
we need to verify that this is actually Htp, so we're injecting the protocol is something that makes sense. So that's why it runs this protocol detector
that does a little bit of checking here to ensure that it looks like Htp.
And then
it looks at this information and then jumps into a program that's gonna write this transparent, this tail call jump is made because these become too big. So we
we can't fit them in a single Bpf program.
But essentially, what you're gonna see, here is what you expect in the
typically in, as in the previous case, we're gonna what we do is we 1st use a Bpf Api to extend the packet. So this is the only place where they let us do this.
This is the only program, this sk message program. So the only places where
the Bpf. Allows us to. Before this packet reaches the Tcp. Stack before the the Tcp. Sequence numbers are computed, and any of that stuff
they let us manipulate the packet.
This was typically done. I think it was contributed by cloudflare for the purpose of actually adding stuff on incoming requests and being able to track in their internal environment.
So one of the operations here is that we can do this message, push data at a specific offset, tell us how much to extend.
and we extend with a fixed size, which is the size of the trace parent column space and the actual value.
and then slash, R slash. N,
once we extend the packet with the right size. If you let us do it, we, this pool data is there to kind of like, bring the data in memory for us to be able to write it. And then we just call this make Tp string, which uses the data pooled
from the context of the maps that were set up by the auto probes.
And then we write this information down, and you can see how it's written here doesn't make sense.
**Nimrod Avni** 29:10 I remember. I think it's something I don't know if we talked about in the previous.
Meaning that
that apps that are already instrumented might like, let's say, I just wanna see if we use the like, the transparent from incoming like already instrumented applications? Or do we need like to remove the instrumentation in order, like what? What part is actually taking the instrumentation transparent.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 29:40 Fair enough, right?
Exactly so.
So this part is the mechanics of how we do the extension and write, and all these things right.
so
the decision what to do, whether to write this or not is all about whether we encode the information in the maps. If we don't encode the information. This code will not do anything.
Yeah, right?
And that this is decided in this massive function here, which is quite complex. And
perhaps it's not like. We could decide if we want to do something better, especially if we want to try supporting an app that's already instrumented. It sort of did support this in the past.
and but the reason why we took it out like I mentioned was that we saw some weirdness in
Istio about what they did, or maybe similar proxies that take the incoming headers, and they just pass them down if you have done nothing, and then they do appear as if they are in the outgoing headers, but it's done by the proxy.
Which is what we we couldn't handle properly.
But perhaps we can if we just simply say, Oh, that's exactly as the incoming header of the of the parent instruction. So then then we should override it, or something like that. I think we can find a way around that problem. But
so, okay, so I said, I'm going to come back to this function, get our craze trace info, which is the key to all the tracing, set up all this information, and so on.
And so
the 1st part part is related to the this sock message. So if we're Http client, and this is written by us, then
we we just say, Don't do anything here. We've already done the work, ignore
But other than that, we do this kind of check. So this 1st part here is something we internally we call black box context propagation.
So this was implemented before we were able to inject headers.
It only works for Http again. It does work for Http and other protocols, too. So you can nest
Tcp and Http, that should still work.
But essentially what it what it does is that? Yes. Tcp also does this too?
it. If both processes are monitored by the same Bela instance, let's say you have a a node, and you have 2 applications on there. They're talking to each other.
But it's a single demon set that's instrumenting both processes.
Then, technically.
we could do this in memory. We don't actually have to pass in any information through the headers.
because we see both the traffic that's outgoing, and we see the incoming on the other side
with the connection, information and the process. Id, we're able to tie those together and say, Hey, you 2 are talking. Here's this unique request. So when you're looking for your
trace information. Look up this map
and find out if some other application that will be is tracking
is potentially set up the other side. This typically happens, if you have a client on one end, it had some trace information set up in for this particular outgoing request. On the other side, you see this?
on the server, which is your auto application. Then you could technically
correlate the 2 and then pass the information simply through a map.
This code. Does that. So it does this checking to see if we can find a client trace or a server request based on this black box propagation. If you dig into this functions, they end up just looking at maps. There's nothing in particular going there.
So so one thing we have here is so this tc, tp, parsing
when we say we want to skip the parsing.
Now, this is only done for Ssl requests.
But technically we could in here if we wanted to support
reusing the trace information that's set up by the application itself rather than using our own, we would have to actually do the information. Do sort of this parsing of the header information right here.
So in this particular
sort of code here, it doesn't care, if you look whether this is an incoming request or an outgoing request
it would go through.
And
look for the header information using this Bpf loop. The only thing is we've added this. This is for the Istio stuff.
and it has, like Istio, for example, having forward headers, as is
so, it looks for a type client, and if
and it's only doing it for Ssl, because I think Istio does Tls by default.
It says, don't parse these headers don't look at them.
So
maybe in Hotel Demo it should have worked, and we should actually check to see if why, it doesn't work, because I don't think they're Sl. Tls, but maybe because the Grpc we make up our own. And we don't parse the Grpc protocols
so maybe we can look in there and see see what's going on.
But this code here should be provided. It's kernel 5, 17. Go look! And if it did find the information. It will override
the information set up by everything else, and pull that and make that the default essentially
But you can see over here the skip was added. Because of this Istio stuff
only for outgoing requests for incoming. We still parse it for outgoing. We we don't.
And
yeah. So I think if we want to use whatever the application, provided we would need to make sure like, does this code work for Http
and right similar one for Grpc. If we needed to support the Grpc protocols within the Hotel Demo.
**Nimrod Avni** 36:35 Cool, and that sounds good. That makes me.
Understand in a bit.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 36:41 Okay? And so this is the main sort of function. There's 1 more approach to context propagation which I didn't talk yet about between services
and that we primarily use for Tls and protocols where we cannot encode the header.
technically, the protocols we cannot. The encoder header. I'm not sure how many of them are, but technically you could potentially correlate between a client SQL. And a remote SQL.
like, I asked this question to you as well, Nimrod, in the issue you made about Mongodb. But we could technically implement Mongodb context propagation or distributed tracing
with ob if we supported the Mongodb server requests.
And the reason why that works is that if
we couldn't use this Tp injector.
so let's say the protocol is unknown. It's not one of these that we recognize. And currently we only recognize Http.
**Nimrod Avni** 37:49 Hmm.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 37:51 But let's say some Tcp protocol grpc, doesn't do anything but Tcp does.
Or it's Tls like, let's say, this is Ssl. What we do here
doesn't work for Ssl, because in Ssl. At the level of the socket information before this
information is passed down to the Tcp. IP stack in the kernel
where the traffic is already encrypted. So we have no
no place for us to extend this. So this new approach that we have the context. Propagation between services in distributed tracing does not work for Ssl. The old in the old style, in Go does work because we do it at you probes before this meets the encryption.
But in this approach we can't. Because of this, it's too late. It's already been encrypted.
So for this Tp injector, we have a different injector. This is this Tc tracer.
So this attempts to encode the information in IP options.
So on Tc, egress. That's where the majority of stuff happens
is that we found an IP option that was unused, or that we could leverage for both ipv. 4 and ipv. 6,
where this information that's set up by this outgoing trace map.
if it may eventually ended up here, means that we recognize, maybe the protocol that we want to do this
distribute tracing context propagation. But we couldn't do it the traditional way, so we couldn't. It was encrypted, for example, or it was a Tc protocol where we don't
actually know how to encode this information. Let's say it's a Kafka service passing this down, or somehow.
So what we do here is we update the information in in this
IP options. I don't know if there's another. I think it's this. Tcp, cip
parses the options, and then it does this inject. It's really low level. I don't
think we may have internal design, dog that I think we can share right now.
About how this was done. There was a couple of iterations we attempted initially to use Tcp options.
but then we found there's not enough space
extending the Tcp package is really hard
because there's no Bpf support for it. So you would need to extend it. The full package move data, recompute checksums and all this stuff
it was much easier to do in IP options.
which it's not to say that we cannot do it with Tcp options, but it's a little bit harder
to do. So right now it's passing an IP options.
The downside with happy options is that if this is going in some through certain like
network equipment they may get stripped beside the options. So it's not bulletproof. But if we couldn't encode it, this trace parent information gets encoded into the IP packet, makes it on the other side, and then this Tc tracer
on the ingress pulls that information, parses it, and then sets up a map
again to be used by that same function that I mentioned here.
This map.
And you can see this map is just check that
When we say find trace for server request.
I think it will try to find
it says incoming Tcp info. That should be IP.
Right.
This is the place if you found incoming trace map. This was set up by the IP options.
Pass your information.
Now, this work with a Tc like has its limitations. It's not ideal like, I said. One option is like possibility is you have certain type of a network equipment that strips IP packets even though it's told not to like the option of using. They may. It's at the discretion. Sometimes
they may change the IP packet.
Any proxies that replay packets. So they're not actually using the original packet, but they will be replaying it.
will also like this can go through.
The other thing is like this.
It uses tc.
so traffic control and traffic control may not be usable on a certain system. Let's say you're using cilium, and then you have certain configurations, you can make it work
and so on. But the gist of it is that if those things are okay, then maybe we
we managed to make it work.
That's why we have the the various modes for context propagation. This is all which attempts both, but you can choose to go with headers only, and not mess with the Tc packets if you don't want to. Yeah.
**Tyler Yahn** 43:25 Cool. Yeah, thanks, Nicola, for that in depth overview that that's definitely a lot. I appreciate that. I'm looking at the time. Right now. I'm just wondering if we wanted to
pause here, and and we can move on to some some other agenda items. But I wanted to make sure if there's any other questions. Last questions before we we do that.
we can get those asked.
**Nimrod Avni** 43:51 Think I'll need to replay the recording a couple of times before we get it. But.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 43:56 That's also yeah. Also an option. Right? Yeah.
we can. We can get a hands on session. We can kind of look at logs together. If you want, like, I'm open to that like anytime. Just message me. And yeah, we can just
go and see what happens with one transaction, and I can walk you through the logs and all that.
**Nimrod Avni** 44:14 Yeah, no, that's really cool. Because we as like, when trying to explore a bit like how how the the context propagation actually works between like the auto demo services and production services. I wanted to
like, see, like the edge cases when it does the work when it doesn't.
But that's like a really cool explanation and implementation.
**Tyler Yahn** 44:39 Okay. Well, cool. So next up on the agenda Nimrod, I had you giving the demo of the demo instrumentation. Yeah, I don't know if 15 min is enough. Do you think that that's fair?
**Nimrod Avni** 44:53 Yeah, I don't know. I can. I can do it quickly. Maybe if people like
like, if we want to go over like a bit of the like edge cases and stuff together. I can show you like the start of what we try to do. By the way, thanks for Mario and Rafael. Help me with debugging an issue.
**Tyler Yahn** 45:15 Okay. The other option is is, we can wait till next meeting, and we can just try to start with the the demo and get more in depth. If you think it's gonna take more like, if you can go more than 15, I I think we should probably do that.
**Nimrod Avni** 45:26 Yeah, I think we can do it. We can do it next week. It sounds good.
**Tyler Yahn** 45:30 Okay. Alright. Then I'll I'll I'll make sure to bump that to to next week, then.
and maybe instead, we can just finish by doing a nice review of what we have for our open Prs, and just make sure we have a status update. And then, yeah, that way, we're not crunched for time.
Okay, I will move this here
awesome. So then, if we want to take a look at the open Prs.
1st up is this bump the X net.
Oh, yeah, we needed to make a exception for this. I don't remember exactly where we found. Yes, Nicola, this is something that you were. Gonna take a look at. I'm guessing it hasn't been addressed yet right.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 46:21 I haven't got time.
**Tyler Yahn** 46:22 Yep, no worries the initialize the host. Info metric on 1st span. I don't know if the author's here.
**MM Mario Macias** 46:30 No, he! He is a colleague from from Grafana.
We. We ask it. Few changes, few additions. He contacted me yesterday, Prevailly that he will. He has been busy with other things, but he will, he will add the the requested changes.
**Tyler Yahn** 46:51 Okay, yeah, that sounds good. Yeah. I imagine. Given all the reviews, the draft removing the draft status was a good idea. So I agree with you on that one.
Okay.
Next up refactor, the hotel metrics exporter. I saw this one come in just a little while ago, Mario, any looks like you have one review. I'm guessing you're just looking for more reviews on this.
**MM Mario Macias** 47:12 Yes, because this this review from Stephen I I mean he has not the status of approval. So he gave the review. But I cannot, I cannot merge it.
**Tyler Yahn** 47:24 Yeah, this looks like a pretty large change. Is it pretty in depth as well.
**MM Mario Macias** 47:30 Not. Really I don't. I don't know why. How many lines. I don't know if the vendor is is maybe some vendor or not. I don't know.
But yeah, but basically, I basically moved. So it's a factor. I moved some in the hotel metrics porter. I had to move some components to another package to separate different exporters. We were fixing a back, we realized.
in which different kinds of metrics should be reported as different kind of resources. So we needed to separate those those metrics generations in into exporter nodes.
Then I started to get some conflicts.
Yeah. So I I did the refactor of moving things, but also
I did an extra refactor to allow that all the different exporter notes for the different kinds of metrics use the same open telemetry exporter
because I realized that currently, for example, application level metrics are network level metrics used different exporters that mean different connections
and different configurations at the end. So I I also added,
a common way to to pass a single exporter to all the hotel exporters something similar that we already did
with the Prometheus Exporter. The Prometheus exporter receives a a Prometheus factory, in which you can create a new Prometheus connection, or reduce the existing one. So this is
similar. Yeah.
**Tyler Yahn** 49:18 I see so is go ahead.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 49:23 Yeah, I wanted to give a little bit more context of the why. This, we found out that there's a spec
line. So we're saying I can find it. But if we, when we generate this span metrics.
any attributes that we put in that are not
one of the default ones, which is like clients, server and server, namespace, client namespace must be prefixed with client or server.
Apparently there's a rule I didn't know of this, so our resource attributes were going as is.
So. It wasn't according to the spec.
There's something saying that service graph metrics, if you are
any attribute that's not in this list must be prefixed with a client or a server.
Something along those lines is in the docs, for the hotel processor.
**Tyler Yahn** 50:17 Hotel.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 50:18 Yeah.
**Tyler Yahn** 50:19 Hotel Processor.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 50:20 Yeah.
The auto service auto collector service graph processor. I think there's some docs that say.
**Tyler Yahn** 50:27 Is you said. It's in the specification.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 50:30 Yeah, it's in the doc somewhere. Somebody pointed me to that.
**Nimrod Avni** 50:32 Probably in the collector. I'm guessing.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 50:35 Yeah.
**Nimrod Avni** 50:35 Or something.
**Tyler Yahn** 50:38 Okay.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 50:39 There's something about this, any extra attributes. And we put in extra attributes. For example, we put in the Kubernetes cluster name, which is kind of helpful, and people want to filter spam metrics, and they want to choose the cluster.
**Tyler Yahn** 50:52 I mean. Obviously it makes no sense to be on the same cluster.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 50:56 To kind of have everything jumbled up together. But that label is not prefixed correctly.
I can find the wording. I think I have someone.
**Tyler Yahn** 51:08 Hmm.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 51:09 Oh!
**Tyler Yahn** 51:13 Okay. Well, I I think, yeah, I think this just needs more eyes on it for sure.
This is a little odd this.
So so, Mario, I yeah, I'm not sure why. So you think this shouldn't be
2,000 lines of code change like, it seems like it's adding a brand new.
**MM Mario Macias** 51:35 Yeah, maybe. Yes, yes, because I moved some some Co.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 51:40 Stuff is moved around.
**MM Mario Macias** 51:41 Yeah, it. It actually surprised me so many lines. Yeah, yeah. But yeah, it can be.
**Tyler Yahn** 51:46 Copied? Or is it? Is it moved.
**MM Mario Macias** 51:48 Most. Some files are moved.
and some code is cut and paste into into new files because it was not just moving the file. Sometimes it was taking for from existing files. Yes.
**Tyler Yahn** 52:05 Splitting them, splitting them. Okay.
**MM Mario Macias** 52:06 Split in. 5.
**Tyler Yahn** 52:08 Yeah. Oh, okay, alright, alright. That makes a little more sense. Okay.
okay. So then, I think this needs just more review at that point. Yeah.
Yeah. Okay.
okay, yeah. So people on the call, please don't get shied away from this. This should be copy pasted stuff. So if you have time. Please take a look, and we can review that.
Okay, next up postgres support prepared statements.
**Mattia Meleleo** 52:36 Yeah, this is pretty much done. There are some odds test failing which I'm investigating. I also addressed the Raphael comments. There is one other thing to do this last comment.
Yeah. I also fixed the the test, because when I 1st started changing this, I noticed that there was the prep query endpoint of the test.
So I uncommented the test, and it was passing for some reason. And then I noticed that it wasn't really using prepared statements. So I changed the the test to
to work with prepared statements.
**Tyler Yahn** 53:20 Cool. I mean, that sounds that sounds great.
Okay. So Raphael looks like you've taken a look at this. Is this just looking for another round of reviews.
or I guess you you've already provided some feedback.
**Rafael Roquetto** 53:35 I think. Yes, you know, as soon as this tests are fixed. And yeah, we're good to go.
**Tyler Yahn** 53:43 Okay. Yeah.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 53:46 Yeah. Okay.
By the way, where do you want me to paste that if you want for that? The labels, the previous issue that Mario is working on.
**Tyler Yahn** 53:54 Oh, yeah. Probably just in the the agenda, Doc. Maybe just so that we don't lose it when the Zoom Meeting ends.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 54:02 So, yeah, thanks for thanks for finding that. Nicola. Yeah, I'm interested in looking into that.
**Tyler Yahn** 54:10 Okay. Last one add internal metrics for avoided services.
This is from Mark. I don't think this Mark's on the call.
Nope. I don't see him on the call. Okay, this is looking for reviewers. It looks like this is pretty recent. Yeah, 25 min ago. Okay, so yeah, just looking for reviewers on this one.
Okay, with that. That's all the Prs. Any other topics people wanted to talk about.
**Nimrod Avni** 54:42 Something quick, I think you and Mario may have already looked at that regarding the helm chart.
Pr. Where they're kind of like discussing the naming of like Evpf. Instrumentation is too long, but we can't call it ob, but we can call it.
I can share, like the the link in the in the docs. I can share it in the docs.
**Tyler Yahn** 55:09 Yeah, maybe we could just take a look at that really quick.
**Nimrod Avni** 55:11 Good here, la!
Like I I think they it must be prefixed with open telemetry, even though the repo is open telemetry.
and I don't know, he suggested. Ebpf instrument open telemetry. Epf, insert
like, I don't have a a
preference. It's just kind of guessing. It's kind of weird to have like
we have Abpf instrument. We have obi, and we have open term Gbpf instrumentation. Then we're going to have another one
for the helm chart
like, I'm not sure why the even the full name. I don't think it's that long.
I'm sure. But it might be like, I don't know long if you try to.
I don't know if it's appended to like a pod with a
like a replica set, and an Id might like fill up the whole thing that's maybe like a concern.
not super sure.
**MM Mario Macias** 56:20 Oh, yeah.
**Tyler Yahn** 56:20 Yeah, I won't.
**MM Mario Macias** 56:22 Yeah. But I mean for me is, is is okay. Let me need
whatever the convention is. If it has to be open telemetry evpf, instrument.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 56:35 Let's use the full name.
**MM Mario Macias** 56:37 No.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 56:38 Yeah. That'll make more.
**Nimrod Avni** 56:41 Yeah, that I fixed most of the stuff there.
We can do.
**MM Mario Macias** 56:57 Maybe instrument open telemetry, Vpf. Instrument to match the executable, the binary, and so on. And it's a bit shorter, not much.
**Tyler Yahn** 57:08 Yeah, I.
**Nimrod Avni** 57:11 I don't know.
**Tyler Yahn** 57:14 Think that's fine.
I mean, I think if you put instrument like.
then you could just do inster you could do. I don't know, it seems. What's the other
other helm charts for instrumentation.
**Nimrod Avni** 57:27 Because there's open telemetry Ebpf which they stole from us.
You could have named that the network Project.
I'm not, if the like. There's probably gonna be something of the
filer, but I don't know. Maybe it.
**Tyler Yahn** 57:44 Yeah, I'm wondering, yeah, exactly.
**Nimrod Avni** 57:47 The Qbpf. Profiling.
I don't know.
**Tyler Yahn** 57:50 This seems like they have a precedence also for using full words in each.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 57:54 Yes.
**Tyler Yahn** 57:55 So I think that I think.
**Nimrod Avni** 57:58 Think it's probably the full name as good as we can.
**Tyler Yahn** 58:01 I think of that seems fine to me. But I don't.
Yeah, okay, I don't. I don't know what to say. There, I think that that's just kind of bike shedding to the point where it's not really being helpful anymore.
**Nimrod Avni** 58:16 But.
**Tyler Yahn** 58:18 That's just me.
okay, yeah, thanks for bringing that up. I think that's yeah. Let's try and let's try and make that move forward.
If you need more help on that one definitely, I think posting in slack could also be helpful. I'll try to keep an eye on that, too. But thanks for walking us through.
**Nimrod Avni** 58:33 No.
**Tyler Yahn** 58:35 Okay, coming up on the last minute. Okay, I think that's probably it for today. Then thank you. Everyone for joining. Appreciate all the hard work. If you have more topics, please hit them up in slack. Also join next week to see the demo of the open telemetry, Demo. I'm excited about that, but otherwise yeah, I'll see you all in a week's time, or asynchronously. Oh.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 58:55 I just had one thing that I wanted to mention that we think we have 2 ob cube contacts accepted. So Tyler and myself gonna talk about it, and I think Mario has another one accepted
with someone else. So so there's gonna be a lot of ob at Kubecon.
It's kind of good.
**Tyler Yahn** 59:17 Yeah. So join. Come come to.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 59:19 Can we keep going? It's all.
**Tyler Yahn** 59:21 So Atlanta in November, which is amazing. So yeah.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 59:25 It's listening to me. Crap!
**Tyler Yahn** 59:27 Yeah, yeah, okay, everyone. I'll talk to you all later. Bye.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 59:31 Bye.
