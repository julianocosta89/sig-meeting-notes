SIG: CI/CD SemConv SIG
Date: 2026-09-29
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Christophe Kamphaus** 06:22 Hello.
**Robert Pająk (Splunk Inc.)** 06:36 Hello?
**Christophe Kamphaus** 06:42 Hello?
**Robert Pająk (Splunk Inc.)** 07:52 Hello?
I will be… I'm on my way with my daughters. to addition, like, to some, you know, additional faculty classes, so I'll be just, you know, trying to listen to you in the background and react if necessary.
**Christophe Kamphaus** 08:12 Okay.
I had a question for you, Robert, actually. It's about the environment variable.
Sure.
I was wondering… Could you have… environment variable propagation and HTTP context propagation.
Enabled at the same time.
**Robert Pająk (Splunk Inc.)** 08:35 Yes.
Yes, because the carriers are usually kind of bounded to some kind of instrumentation, so these are two separate things. So, if you have, for instance, an HTTP instrumentation, it uses headers, you have some, you know, other mechanism, it will just use environment-verb carriers, so these are not mutually exclusive.
**Christophe Kamphaus** 08:57 Okay, so it would depend on how those are configured in the instrumentation, the order.
**Robert Pająk (Splunk Inc.)** 09:02 Exactly.
**Christophe Kamphaus** 09:04 Exactly.
**Robert Pająk (Splunk Inc.)** 09:04 you.
**Christophe Kamphaus** 09:05 It was what I figured, but I just wanted to double-check with you.
**Alan Clucas (Pipekit Inc)** 09:10 So there's a… I mean, you can obviously propagate Via one mechanism, and then via the other, so… Yeah, got various… It sort of happens in Argo.
Only there's not a super good demo of that happening in a useful way. But in theory, once we've got tracing in Kubernetes.
the traces will propagate through environment variables, and then into Kubernetes via HTTP, and you'll be able to, like, go. That's not exactly what you're asking, I know you're thinking about both inbound, but you… you definitely would… you'd get a combined trace across all of them. And it kind of happens in the Buildkit demo that Robert and I are going to present it.
**Christophe Kamphaus** 09:58 Oh, nice.
**Alan Clucas (Pipekit Inc)** 09:59 So, building kits, doing HTTP, providing Http traces which carry the stuff. But there's nothing. The the repo server doesn't do tracing that I'm aware of. Oh, that'd be a good… that'd be a really good demo. If the repo server did tracing, then when you just propagate into Buildkit with environment variables, HTTP propagation to the repo server, and then the repo server could emit spans for what's happening.
Inside it. Hmm.
Oh, you've made me want to try it with Harper, see what Harper does. Does Harper do tracing?
**Christophe Kamphaus** 10:32 I was wondering that myself just now.
Yeah, maybe to give some context why I was looking into it.
For, both. Let me share my screen.
So, I prepared some… prototypes for this PR, the VCS span semantic conventions.
And, yeah, feel free to review it if you have some time.
I did it once for the Jenkins OpenTelemetry plugin, and also for the Git trace to receiver.
Which is an, open telemetry collector receiver that takes trace 2.
Format.
coming in.
And that's the format that the Git CLI can emit.
**Alan Clucas (Pipekit Inc)** 11:22 I didn't realize you'd done that.
That's nice.
**Christophe Kamphaus** 11:25 Yeah, I just pointed Claude at it, and it was nice.
It did have some limitations.
like, Git does not support environment variable carriers yet, so it cannot propagate those, and that's where I was thinking of What if you start the receiver, the hotel collector, with the environment variable?
context.
Of course, you would have to start it before launching the Git CLI command, but it would be a workaround.
And then what if you later also could receive it via the trace tool itself? Or would that?
Fit together.
But yeah.
**Alan Clucas (Pipekit Inc)** 12:10 So this would do… this is sort of… You're backfilling the traces.
because Git's not natively in the tracing chain.
Any HTTP requests, for example, aren't ever going to really get them.
**Christophe Kamphaus** 12:25 Yes, so
**Alan Clucas (Pipekit Inc)** 12:26 propagate.
**Christophe Kamphaus** 12:27 On server side, it would only work if you go with… Git commands over HTTPS, so there you could have the headers, and then it would be on the server to support it on server side.
Here, it's really on client side.
Where you can see the different operations that Git itself does internally.
Like, for example, it, a Git clone does perform two Remote calls, wants to clone.
And wants to, fetch the actual, archives.
And then it also performs local operations, like a checkout.
And that's not shown here, because… in, Git's Internal representation, it's a separate operation.
**Alan Clucas (Pipekit Inc)** 13:28 Thanks.
**Christophe Kamphaus** 13:34 Yeah.
Here, it's just ceased to, Spans that were added that actually, implements the VCS span conventions. That's also why it's shown here.
as outgoing calls to GitHub.
with these attributes.
Any questions?
**Robert Pająk (Splunk Inc.)** 14:10 Can you… Add this or to the.
to the agenda notes, so I can take a look later.
**Christophe Kamphaus** 14:19 Yeah, I can add it to the agenda. There's none, no items on it yet.
So if you want to discuss something, feel free.
Is there anything to discuss?
**Adriel Quinn Perkins (W.W. Grainger, Inc.)** 14:59 I came a bit late, but I assume that was the VCS demo and that the VCS PR now is, is ready to be re-reviewed.
**Christophe Kamphaus** 15:06 It's ready to be reviewed.
I showed…
**Adriel Quinn Perkins (W.W. Grainger, Inc.)** 15:09 Thanks for all that.
**Christophe Kamphaus** 15:11 Prototypes.
And this one is the Git CLI one.
So you see the internals on… of a Git clone operation.
Yep, if there's… Nothing else, I will see you, Alan and Robert, next Monday, so I will attend.
Observability Summit.
**Robert Pająk (Splunk Inc.)** 15:52 Now I'm getting nervous.
**Adriel Quinn Perkins (W.W. Grainger, Inc.)** 15:57 students.
**Robert Pająk (Splunk Inc.)** 15:57 Yeah, but honestly, yeah, very cool, thanks.
**Christophe Kamphaus** 16:04 Great to see you.
**Adriel Quinn Perkins (W.W. Grainger, Inc.)** 16:06 I got one quick thing, if that's okay.
**Christophe Kamphaus** 16:08 Yeah, go ahead.
**Adriel Quinn Perkins (W.W. Grainger, Inc.)** 16:11 This is just a ask slash… Thought, you don't have to answer now.
But I'm curious if anyone here has appetite in helping maintain some infrastructure for the tracing stuff, a long term, within the OpenTelemetry community.
And for the last two years, I've just maintained it, and it's still technically just maintained by me.
And I'm fine with that, but I also wouldn't mind help, so… It's basically just some automations that run in the cloud. That, You know, have telemetry flowing through it, and then now we're adding Actually, some of the shared workflows to be able to propagate that.
**Christophe Kamphaus** 16:54 account.
**Adriel Quinn Perkins (W.W. Grainger, Inc.)** 16:54 text and pass over to it. But if anyone.
Think about it, you don't have to answer now, but if you have a… Yeah.
**Christophe Kamphaus** 17:02 I'm, I'm open.
I'm open to it.
**Adriel Quinn Perkins (W.W. Grainger, Inc.)** 17:06 Cool.
Awesome, Ben. So yeah, if anyone else, too, feels like they'd like to, just let me know.
And I'll, I'll figure out the best way to, like, open the automation up to us, but I think it'd help with the long-term Support of that, and the tracing of… All the other things we want to add, so…
**Christophe Kamphaus** 17:29 Yeah.
**Adriel Quinn Perkins (W.W. Grainger, Inc.)** 17:30 Mercy.
**Christophe Kamphaus** 17:31 As it sounded, the biggest roadblock is actually the vendor neutrality of OpenTelemetry itself.
If we want to open it up to some more.
People in the organization can consume it.
**Adriel Quinn Perkins (W.W. Grainger, Inc.)** 17:48 Yeah, forward back, yeah. And I think that's kind of… Right, that's kind of why I'm asking to see if anyone else would like to… And it means my job because.
If we choose a vendor, I don't really care. Like, the maintenance effort is low.
But once we start self-hosting backends.
the maintenance level is no longer low. It becomes harder, right? And it especially, like, depends on what type of backend, like.
you know, We do Percy's. We're talking about custom development.
If we're talking about actually, there's like almost no vendors that don't that really truly meet the requirement of like Oss and not vendor box Oss. So we'll have to figure that out later. We haven't gotten a decision from the Gc. Yet, but when we do.
We should be able to have information on which direction to go, and if it's the hey, we need to maintain some open source components.
That's where, I think, maintenance will really help.
**Christophe Kamphaus** 18:58 Yeah, definitely sounds like a GC decision there.
So, backend, where I think it might be closest, would probably be OpenSearch.
which is also a Linux foundation project.
Yeah, but let's see where it is.
**Adriel Quinn Perkins (W.W. Grainger, Inc.)** 19:23 I agree. That's the only one that really meets.
No.
whole requirement.
But having maintained it before and run it before, it's a heavy… it's a heavy lift.
It's a heavy lift.
**Christophe Kamphaus** 19:38 I run some Elasticsearch with the ECK operator. I don't know if that would work with OpenSearch.
Or if they have their own.
**Adriel Quinn Perkins (W.W. Grainger, Inc.)** 19:50 I don't know, I can look into it. You said the ECK operator?
**Christophe Kamphaus** 19:55 Yeah.
**Adriel Quinn Perkins (W.W. Grainger, Inc.)** 19:56 Is that a CATES operator, basically?
**Christophe Kamphaus** 20:04 Oh, it's this one.
It makes it pretty easy to run Elasticsearch on Kubernetes.
**Adriel Quinn Perkins (W.W. Grainger, Inc.)** 20:14 Good luck.
Alright, cool.
Yeah, and if that becomes the option that we have to do, like, if we want, like, some… if some of the easier stuff is on Kubernetes, we'll… probably want Kubernetes view on the way that I did it.
I like the way that I did it, but it is… very thin, because it is just K3S on the node.
Single mode. But if we're talking about multi-node stuff, then we may want to use a… we got options, but, yeah, once they make their decision, I appreciate… appreciate the support, for sure, and the volunteering there, Christophe.
**Christophe Kamphaus** 20:57 Yep.
Happy to help.
And for sure, if we are talking about hosted applications, for sure there's a cost to that.
See ya.
Anything else?
And…
**Adriel Quinn Perkins (W.W. Grainger, Inc.)** 21:28 Oh, just to recall out, if you're looking for, wanting to get into the open telemetry collector world, two components are looking for more Code owners and support unless they get loud and get hover series.
Now I'm done, like, officially, for sure, this time. Promise.
**Christophe Kamphaus** 21:50 You can post the links to them here.
**Adriel Quinn Perkins (W.W. Grainger, Inc.)** 21:54 Sure, I'll put them in the notes.
**Christophe Kamphaus** 22:20 If nothing else, then… I'll give you back your time.
Have a great weekend. See you next Monday.
**Robert Pająk (Splunk Inc.)** 22:30 See you!
It almost…
**Christophe Kamphaus** 22:32 Alright.
**Robert Pająk (Splunk Inc.)** 22:32 see.
**Alan Clucas (Pipekit Inc)** 22:33 Alright.
**Robert Pająk (Splunk Inc.)** 22:34 Yes.
