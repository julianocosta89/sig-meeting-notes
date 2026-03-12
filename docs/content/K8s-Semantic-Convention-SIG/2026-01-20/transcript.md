SIG: K8s Semantic Convention SIG
Date: 2026-01-20
Duration: 11 minutes
============================================================

## Zoom Recording Transcript

**Alan Clucas** 00:13 Hello?
**BhupinderSingh** 00:17 Hi, Ellen.
Good morning.
I'm new to hotel, actually, like, to this… these sessions.
So just join in for learning.
**Alan Clucas** 00:30 This is my first time in this one.
Okay, quick.
**Christos Markou** 00:47 Hello.
**Alan Clucas** 00:51 Hello.
**BhupinderSingh** 00:52 Bye.
**Donal O'Sullivan** 02:07 Hello?
**Alan Clucas** 02:10 Bye.
**Dmitrii Anoshin** 02:39 Hello, everyone.
**Christos Markou** 02:44 8.
That's… I'll give it a couple of minutes, and then we'll start.
In case anybody else will turn.
Okay, I guess we can start my… The first issue, the first item in the agenda is mine.
And, it's mostly an FYI. I filed the PR a couple of days ago to promote the selection of Kubernetes attributes.
To better stability.
there was a PR, before the vacation, the holiday break.
to promote them from development to alpha, that was merged, and there was a recent release of the cement conventions that was published, I think, last week.
And out of these, we were able to use this latest version of semantic conventions in the Kubernetes Attributes Processor already.
Nothing breaks, everything seems fine. So now we are on a fresh main, and I filed the PR to promote from Alpha to Beta. This is mostly to advertise the intention that we're willing to proceed with the graduation of this.
set of attributes. I'm not touching the entities themselves, I'm only changing the attributes within the registry, because I think… Maybe that's what we will need for the processor, mostly, but we can discuss this.
So, yeah, feel free to have a look there. And, this is mostly work that is needed for the… work that we're doing for the KHAT, which processor, too.
have it as V1 soon.
In the following.
Hopefully months, I would say.
Yeah, any questions?
Comments.
Okay, let's wait for the, let's wait for reviews then on the PR and see.
What will, get there.
Thanks. Next one is… Alan?
**Alan Clucas** 06:34 Hello. I've not been before. I'm really only here to get… see if anybody's got any prior art, anybody knows anybody else who's doing something similar to what I'm trying to do.
I'm one of the maintainers of Argo workflows, and I'm putting tracing in, so I'm mostly working with CICD, SEMCOM, for… how to, so, Argo Workflows runs… it's like an elaborate job controller, it runs workflows through Kubernetes, and so CICD maps quite well for running… for annotating an individual workflow. but it runs as a controller, a standard sort of Kubernetes controller.
And workflows is, quite… capable of killing a Kubernetes cluster in such a way as that things like leader elections and, informers get, get upset. So, I have added tracing to the That the, the API calls into Kubernetes, and that's very useful when they are related to a workflow that is running, but there… there are also things like leader elections fail, and I'm generating leader election spans for the question… the queries throughout the Kubernetes Leader Election API, and things like informers, I can see the watches, and when a relist occurs, because relists are generally bad, we're running standard ClientGo informers.
I'm hoping some of this makes sense to some of you guys, and I'm wondering if there's any prior art in, Grouping together these spans so that they're not a bunch of Individual route spans for each query, or whatever.
I've done something, but it, it felt wrong And, This felt like a possible forum where somebody had come across Kubernetes operators being Modified in this way, but…
**Christos Markou** 08:53 I think, the… yeah.
I mostly understand what you're describing. I… the purpose of this group, though, is mostly around.
**Alan Clucas** 09:05 I never…
**Christos Markou** 09:06 Working on the semant conventions of Kubernetes.
So, maybe we can discuss this, or… I don't know, Dimitri, if you have any, ideas or anything. But what comes to mind is either the Kubernetes Instrumentation Working Group of the Kubernetes community.
I will look for the link to share this with you, because I know they have done, like, instrumentation on, I think, Kubelet, Kubernetes API Server, for sure, maybe Kubelet as well, so maybe they can, give you better you know, guidance there. Or, then maybe our operator SIG, OpenTelemetry Operator SIG, in case they are… They have dealt with something, similar to, that's what I could think.
**Alan Clucas** 09:57 I know the operator somewhat. I've done some PRs for it, and, so far I haven't found anything related to this, so, okay, that's really what I was here for, was… I wasn't expecting, unless one of you happened to do that as well, because I understand this is a SEMCOM, but I felt like a… adjacent thing.
Thank you, I will… visit.
**Christos Markou** 10:22 Yeah, I sent you the link here in the chat. We also have it linked in our community as, like, a relevant group.
So maybe they could help you.
**Alan Clucas** 10:34 Thank you.
**Christos Markou** 10:37 Dimitri, you were going to say something, or…
**Dmitrii Anoshin** 10:39 Yeah, I just want to conform to what you said. I want to mention that Kubernetes have their own SQL observability.
Specifically. So, let's go back to their premises.
**Alan Clucas** 10:54 That's… that's brilliant. I didn't know about that one, so thank you.
**Christos Markou** 11:08 to, anything else from anybody? I don't have any other updates. I think mostly the focus now is work on the KH attributes processor and relevant work on the semantic conventions.
So… That's mostly what I'm focusing on.
But if there is anything else that we should look into, just let me know.
Okay, there is nothing else we can wrap up earlier today, I guess.
**Dmitrii Anoshin** 11:43 Sounds good.
Thank you, of course.
**Alan Clucas** 11:47 Thank you.
