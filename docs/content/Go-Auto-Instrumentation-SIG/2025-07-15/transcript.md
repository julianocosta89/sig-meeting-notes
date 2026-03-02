SIG: Go Auto-Instrumentation SIG
Date: 2025-07-15
Duration: 46 minutes
============================================================

## Zoom Recording Transcript

**Tyler Yahn** 00:34 Hey! Raphael!
Hey! Nicola!
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 00:37 Hey!
**Tyler Yahn** 00:43 How y'all doing.
**Ron Federman** 00:44 Hey!
Great!
**Tyler Yahn** 00:49 Raphael, did you get a grinder yet?
**Rafael Roquetto** 00:52 No being
starting with the one you you know the link you sent me. I'm just trying to convince my wife
that it's a you know the Prices Price tag is worth it. Maybe I'll get it for Christmas. I.
**Tyler Yahn** 01:06 I was. Gonna say, the way you do it is you say it's your hobby, and
And all of a sudden, yeah, you know, has nothing to do with that. Yeah.
**Rafael Roquetto** 01:14 Yeah, yeah, that's a good idea.
**Tyler Yahn** 01:18 It's a hard one. It's it took me years to commit to buying something so expensive for coffee. Yeah.
**Rafael Roquetto** 01:25 I mean I'm sold on it.
I'm I'm weak, you know. I like it.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 01:32 Where'd you guys talking about.
**Tyler Yahn** 01:34 We're talking about this coffee grinder. It's a fellow ode 2. It's like something from last last time Rafael was telling us how he has like a hand grinder. And I was like, Yeah, I'm deep in the coffee culture area. So we were. I was giving him some recommendations. But.
**Mike Dame** 01:52 Yeah, I remember that.
Yeah, I have a tough time with my grinder.
Yes, no one else got the maroon shirt. Notice for this sick call just me and Raphael.
**Tyler Yahn** 02:05 No, it's the black Shirt Ron and I were we got. We're on a different email chain.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 02:10 Dot yeah black sheep.
**Tyler Yahn** 02:17 Well, cool.
Looks like everyone's here. I can start sharing my screen just a second. If you haven't yet. Please add your name to the attendees list, and if you have agenda items to talk about, please go ahead and add them there as well. Yeah, we can get started here.
Awesome
all right. So to start us off, I wanted to just kinda follow up on the conversation from last week and just talk about this idea and make sure we're all on the same page for this integration phase one, we're unifying epf programs ideally from here. The follow up is we, wanna you know. Take this as a starting point and then iterate on it. Obviously we have bigger goals in mind. So this is explicitly stated as phase one I didn't really.
let's see, I didn't really contribute much here. I was mostly just capturing what Nicola had already written.
so it should should look very familiar, essentially starting with a single probe
and then updating the probe to make sure that it works in both this project and in the Ebpf project. In fact, Nicola has done a little bit better job below talking about the steps that he's working on at this point to create that process, Nicola, is there anything you wanted to say? Maybe on this.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 03:39 No, no, I just broke down the tasks into something that I was planning on. Kind of starting, like Pr. By Pr sort of
to see how close I can get
and see where that takes me.
If you guys prefer that I work on a separate branch, maybe that's awesome.
**Tyler Yahn** 03:59 To your better.
no, I so that's maybe a good question. I think I mean, I'd like it if we could just commit this stuff to Maine that makes sense to me. It. It is it going to break in between Prs, I guess, is a question.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 04:13 No, no, yeah. Okay.
is that it should never break the way I laid it out. It should be like incremental steps, and then
only at the end we switch
right? So go to use this new table, for example, and once that's done
like should never break a note or go. And then hopefully, we can try using adobe, and if still
I will in the meantime
ensure that what I'm doing actually can fit in there on the other side. So.
**Tyler Yahn** 04:43 Yeah, okay, all right, that was my understanding as well. So that makes sense.
So yeah, I think committing to Maine makes sense, especially with what you just described. I think that definitely makes sense one of the things that did kind of like.
you know. Maybe the question is, is also like, where does it fit in a release cycle? I don't think it really matters like you said, though, since it's the last Pr that's actually going to have effective change. This is just setting up the scaffolding beforehand.
But I wouldn't want it, I guess, to block this. I don't think it is going to block this. But we can. We can maybe jump in there after that.
Okay.
But yeah, otherwise. This looks good. I don't know if anybody has any comments. Please go ahead and comment. Here, Nicola, is this something that we can parallelize? I think there's tasks here that they look sequential to me. But I just kind of asked. Maybe like, if there's people that wanted to also help on this.
What are your thoughts.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 05:40 No, I'm like, yeah.
I mean, it's so incremental. But yeah, we can. We can split amongst multiple people. Anybody else wants to do.
**Tyler Yahn** 05:48 No, I think, yeah, that was just my my question. If it's incremental, then I don't. I think that that makes sense to just
do it in secret sequence, then. But yeah, so cool. All right, then, let's let's let's stick with that. Make things less complicated.
Okay.
alright cool. Alright. So then, next up I wanted to check in on our goals. We had set out at the beginning of the year.
and maybe just update these, or see where we're at on these. It's been a while. It's also going into the, you know, halfway through, or more than actually right halfway through the 7th month. So.
getting into the latter half of the year, I wanted to maybe just check in and see where we're at.
So for the Bpf road. Bright user alternative. I don't think there's been any update on that, at least from my side. There has not been. I don't. I think, Nicola and Damien, you've also been looking at this like this is something that you had sponsored, so
I don't think there's been any work.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 06:48 Well, it's going to have to happen if we merge the
merge. The 2 code bases. So the changes from Ob will have to end up here in one form or another to support this, we're gonna have to figure out how to do that.
Yeah, right?
That we're going on this path of merging the code bases at least, and
I think it can naturally flow from there. I hope.
**Tyler Yahn** 07:13 That's a good point. So yeah, saying, nothing isn't quite accurate statement. I guess.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 07:28 Think we've it. Ob cleaned up all the bugs related to that implementation.
We haven't had any new ones, so I should say that people have reported.
So we think it's good, and my attempt
doing it for Grpc. As well.
**Tyler Yahn** 07:52 Yeah, okay, well, cool. Alright. So then, this, actually, I think, is more.
yeah, I don't know how we want to structure this. Maybe this is just a sub goal, or this gets essentially like
combines with. I guess beta integration is not the right term anymore. We can call it ob.
oh, am I gonna make? Oh, no, okay.
Yeah. I think I think that makes sense.
I think this has also become a lot more than just this donation task at this point. So this probably needs to get updated as well. Where is that
could add this here?
What's that?
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 08:42 To put the Republic.
**Tyler Yahn** 08:43 Oh, yeah, that's a great idea. Yeah.
let's let's do that.
That's
perfect. Okay, okay.
cool these 2. We've already accomplished the custom. Probe Api. So this is another one we talked a lot about. I think this is pretty obvious where we're at on this 1. 0, shoot! Hit the wrong button.
We're waiting on this Pr. That needs more reviews. If that's if I'm not mistaken. Right, Mike, this is a part of this this probe Api refactor.
**Mike Dame** 09:50 Sorry I was clicked away. Which was that the the shift process, one that we're still working on.
**Tyler Yahn** 09:55 Yep. Yeah.
**Mike Dame** 09:57 Yeah, I feel like that's
probably all part of the ob you know the the whole refactor that we're doing right now, and I'll I'll probably end up closing my Pr. Too, since there's I think the that was just kind of trying to start the work, and I think now we have more of a plan of the actual work to do. So starting with the the C probes sea level code and stuff. So.
yeah, I I'd say that that is all tied into the ob integration. Basically at this point, are really kind of
almost blocked on it, I'd say, or like a a parallel. You know, goal, since they're kind of tied together like the the custom probe Api depends on an Api that will work with Ob. So those 2 are linked but still distinct, I'd say, linked, but distinct.
Yeah.
**Tyler Yahn** 10:52 Okay, yeah, that actually makes sense. It depends on our findings from the whole. This whole process. So yeah, that makes sense
cool.
I think this is helping understand some things. Okay.
So the next step is the custom handler. Api, I think,
this is gonna sound like a broken record. But it kind of is the same thing, like, I think we have like a proof of concept for what we wanted to do here.
But if we're going to be changing the way that we're processing this by changing the the manager pipeline to support the ob integration, like, I think we want to make sure that, like whatever we come up with, there is going to be supportive of that. I think if there's a great idea
in supporting, like the the P data structure. We had talked about that before. But like, I still think that maybe like we don't know the exact P data structure, we don't know if that's the the best optimal representation for the ob integration. So
I think maybe also, the custom handler Api stuff
is, I think, at a maybe at a stopping point at this point, because we have an implementation here. The only thing left that we had, we wanted to add was something that where we put in a collector to be an alternative implementation of this.
I'm not really motivated to work on that. If we're going to be changing the design of the handler to to work on different integration into the manager. So I think maybe just pausing on this ultimately, like the Ob project, wants to be integrated with the collector. So I think we have the same goals right like that doesn't actually change having 3rd party support for handlers, I think, is a great thing that we could try to support there as well. I think we should try to support here if we can do that as well. But I think again, depends on the manager. So
yeah, I think this one's got a pause at this point.
The binary object file tracking it
don't think that's blocked by the ob integration. But I also don't think that there's any much more of an update than what we've already have. I think this just needs more eyes to go back to it. I think Raphael has done a lot of really great work here, and I think it's all been captured. So I think that there's
there's definitely some decisions that we can make. I think there's maybe still some, some prototyping that we were looking at doing. If I'm not mistaken, Raphael, I don't.
**Rafael Roquetto** 13:16 Yeah, so I mean.
in terms of prototyping, I think that's pretty much it. What we did with with the this Beta Gen. Files like this on on my last comment
one thing oh, it's it's gone.
**Tyler Yahn** 13:35 Brutally, the.
**Rafael Roquetto** 13:37 Probably because, yeah, because it's moved to ob, it's gonna be ob gen files in the ob.
**Tyler Yahn** 13:42 Oh!
**Rafael Roquetto** 13:42 Source trees. But this is the approach that writes to to the theoretically immutable go module. So
what what we should, I may add a comment there what we did for Ob mentioned it already is that we start using sub modules, and we just use
rewrite, I guess is on the go go MoD go dot MoD, so that we can build entry the binaries. And then when did you go? MoD vendor? It will kind of replace replace the directive. I quite like that approach in the beginning. I thought it was a bit strange like, because we have both a sub module
and the actual vendor directory. But it keeps.
it keeps things self contained. And so the source of truth is gonna is is the sub module, and then we just rewire it, and we bypass the go
tooling, and we don't have to deal with any any of the you know work around or any of that. So obviously, it comes with trade offs, and it depends on get sub modules to begin with, and we're doing again something unorthodox. But everything about this is unorthodox. So I might add a comment there to list that. But we're we're gonna have to my opinion we're gonna have to look and decide
which poison we want to drink. And
I don't know. I mean, obviously there, there could be other ideas. I just can't think of them.
**Tyler Yahn** 15:16 Yeah. And I think another
thing that might help us is if we can. You know, the the ultimate goal for this, like custom, probe Api would help split these probes into like smaller repos. Essentially.
I still think you're going to have like, you know, your header files are going to be shared across all of them. So like changes to those are just going to be distributed across all the repos. So you're going to see large changes in like binaries at that point.
but I think that the impact may also be less once we have a little bit more partitioning across this, but it kind of goes back to that sub module thing that you're talking about. Anyway, it's like it. May I think that then you need to have a story around that. So yeah.
**Rafael Roquetto** 15:55 Yeah, yeah.
**Tyler Yahn** 15:55 I think you're right solving it by picking the poison.
**Rafael Roquetto** 15:59 The the sub module approach. I mean, maybe there are other shortcomings we haven't encountered yet with with Obi, because it's
somewhat recent, but it would also give us the flexibility of pinning.
You know, in in the scenario, you're talking about this this other repo. With all these different probes we can mix and match and and gives a completely flexibility on downstream projects of, you know, I wanna stick to this hash. And then I want to upgrade it so they can. They. They can work in different step walk in different steps and different speeds, and and might might be a good idea. I don't know. It took me a while to get used to it, but now that I kind of we've been doing this with ob. I kind of like it, because, like you said, it's
really want. I mean, you gotta embrace, get some modules. I don't know if that's something you want to do, but with that premise
it pretty much becomes this one.
you know, really easy place to manage. Everything else just points to it. So I don't know. I I will add a comment there, explaining this, and we can take it from there. I guess.
**Tyler Yahn** 17:08 Yeah, that sounds good.
**Rafael Roquetto** 17:09 Yeah.
**Tyler Yahn** 17:14 Okay?
Then, next up on the list would be the ob integration which we've talked about a fair amount already. We already have a plan for next steps, including the next phase. So that's documented.
I don't think there's much more to say there
and then last up on the list is sampling. So we have a sampling support issue here. Ron, any update on this we wanted to support custom sampling based on attributes.
**Ron Federman** 17:41 And yeah, so like, I did like all all the different beyonce
I stopped because I didn't want to add any more changes to the probe. Api.
since we're not sure about it yet.
Yeah, because, like the currently, the probe Api has, like some connection to the sampling configuration and
and like I didn't want to add
more stuff that we're not sure about.
**Tyler Yahn** 18:14 So I think that's a good point, like, if this is going to be our starting point of using the the probes and sharing them across the project. I'm sorry the Evpf programs right and sharing them across the project. It might be helpful to have like sampling in the sampling config down low level. Nicola and Rafael, correct me if I'm wrong, is not something that is included in adobe. Right like this is a feature that would come over from from this project.
**Rafael Roquetto** 18:41 That's my understanding. But maybe Nicola.
it's more qualified in that front than me.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 18:50 Sorry about the the sampling support.
**Tyler Yahn** 18:53 Yeah. So so, so like, right now, if we wanted to support like custom, sampling
attributes like sampling by attributes doing trace based ratios and like parent-based configuration and sending that configuration down from the Go space
into Ebpf programs like that doesn't exist in Obi, currently, right? So if we wanted to eventually have that that supported would. I mean, okay. So then, it sounds like having a full featured setup of what we want here so that we could then try to integrate it into Ob might be more helpful. Is that
yeah?
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 19:27 True. Yeah, yeah, okay, that. Yeah.
**Tyler Yahn** 19:30 I think. I think maybe that's actually a good point is like,
so, Ron, I see I see 2 ways. I think
we could try to just build out this custom sampling, because then we know what we'd want for configuration right the other side is, we could try to take what we currently have. And in Nicholas process here of moving the these probes and vendoring moving to Ob, we could start to look into trying to get Obi to use these sampling values by sending a configuration on that side.
And then we have, like a single single place. We would be working on this. I think there's ways we could work on this in in parallel here given. It's going to be down at an Ebpf program, and we're kind of tooling with the Evpf program at that point, or at this point.
does that make sense? Or do you think that it still is is blocked on higher level decisions.
**Ron Federman** 20:25 I mean today, like the configuration is like a
is done like all the way from like from environment, variable, or like the higher level of the go code, and it's part of the probe Api, like from its initial config.
And I also wanted to be able to like dynamically configure the sampling. I don't remember if I added this or not, but I also wanted to do that.
And
but yeah, it's it's like, I agree like we can add more stuff on the sea level. But it it like for now, like, let's say, we have this probabilistic sampling or
price. Id of a ratio sampler. It's like- like you need for for to support new samples, you need to add both the go side and the seaside. So, yeah.
that's that's my point.
**Tyler Yahn** 21:21 Right? I I guess.
Yeah, that that's your point. So so I guess it's a good question. So we're going to be migrating this database probe over into ob right?
Are we going to be supporting? Sampling in ob, I guess, is is kind of like what what I'm getting at right. And how is that going to go? Look right? Because how does that dependency pipeline look? And if we are.
it seems like that's a great time, because this is going to unify that in the same way that Nicola is unifying
like offset support. Right like, do we want to make sure that that is supported over in Obi right now, like the configuration format that you've defined in the Ebpf program like that does that get supported over in Obi.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 21:59 Yeah, we would have to. Yeah.
yeah. And it's it works easier for us, I think if they have an example, how it's done, then we can see it. I mean.
have a approach.
If wrong, you can make something, then we just adapt to that.
**Ron Federman** 22:14 So there's like the set of file that, like all the different probes, are using, like all the different libraries. And there's like a I think it's called Start span
and like, it's a common header, and, like all the sampling logic is inside, there.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 22:30 Inside. Okay, cool. Yeah. I saw that. I mean, I know all of it. Right to work on
total. Go auto. And then
we just have to do something like that and port this over and use it. Yeah.
we'll just do it. There's there's all sorts of alignment that we have to do there in terms of how we share the code, because I mean, even if we do the probe for database to find the parent context for a wrapping Http request, or something like that.
The data structures must match right? That probe is going to look for in a structure right? So Ob must support the same structure in order to
to make that context propagation work. Right?
So it's not gonna be easy, but we'll make it.
We'll make it happen.
**Tyler Yahn** 23:20 Yeah, that that yeah, definitely. So Ron is is what I'm hearing from you like, kind of similar to the
The handler. Api that I was talking about like, do we want to call this this done at this point, and say that, like what we have is like the the functional set that we want to try to then
merge that support over into whatever whatever is consuming these right, like whatever we build this Api from like it needs to support at least this level of sampling. And like, maybe in the future, we add a new goal or a new project, or a new task, to increase that functionality.
**Ron Federman** 23:54 And yeah, think so like the right now, it's I think it supports like the samples that are defined in the spec, maybe, except the the Jaeger one, which is also part of the hotel spec. But but yeah, like the final
final milestone that is reading. There is like a like an extra functionality.
This stuff like may like, maybe during the integration with Obi, we will need to change this sampling Api or.
**Tyler Yahn** 24:27 Right? Yeah, exactly. So if we need to change the sampling Api that we probably don't wanna like, have you know, way, additional features. We do want to keep sure like. Keep in mind what those features might be. But I think, think, having what we have right now, and modifying from here
is like a minimal feature set minimal viable product essentially. And we can try to work on that integration and and say, like
our next iteration for sampling will include other things. Yeah.
okay, cool. I'm gonna close this based on that. And we can cut the scope there. And we can say that we've accomplished another one of our goals
changing the goalpost a little bit. But I think that's fair.
Yeah, awesome.
Okay, cool. Alright. So that's I think all I wanted to check in on here.
That's making progress.
Going back to the agenda, that's all I had for today. We are at 25 min in.
so I can stop sharing my screen here.
Any other topics people want to talk about.
**Ron Federman** 26:05 And I. I wanted to ask about the handler Api points that you mentioned like I. I remember originally we wanted to use P data.
both because of the collective integration and because, like the
and collector exporter, seems to be more efficient if you like. We
talked about creating like a collector pipeline that will export the spend.
So do we feel confident like that, we going to use the data? Or you think maybe we'll change that because the handle Api, as I remember it is, is pretty generic, like the only assumption there is you that you use P data right? Like, if that assumption is correct, I guess it's a valid Api that we can build upon.
**Tyler Yahn** 26:55 So based on, like what we were looking at in in Nicola's overview of the the tracer, the internal data format for, like telemetry data inside of Ob is different, because it has to include.
I think, like process level information. There was additional information that was not included in a P data structure. I guess.
that's not to say that you can't then take the parts that are included in the P data structure and wrap that as well. So like this. This Api, I think, could work in that situation as well, so essentially, the handler could get used over there as well as kind of what I'm thinking, but I'm not 100% sure.
like I don't have a proof of concept of that, I guess, is is what I'm I'm saying
I think it might be more helpful in understanding like development. Wise, if that's going to be the case, I think also that
the
if it is the case right? Like, let's just say, like, we live in a world where, like, we actually want to keep the same handler Api, with like the same data format that's coming through, which is, I think, scope spans right now or at the scope level, right? Like, then, yeah, I think we should just start working on like that. That handler that's going to integrate with the the collector, because
then we can just win both this and the ob integration could just start to be used as a collector integration at that point. Right? Like, I think you get a lot of benefit from there.
And if not, then I think that we want to make sure that like, maybe it's like a resource span level is what we want to actually exporting at.
Then we could try to. Then we could try to work at that level. I think we might.
I think we might be in a little bit more of a tougher situation for the resources, because I think that is going to be
the integration point with the collector may be a little bit different at that point. But I don't know.
I guess I guess actually talking through this like having a proof of concept. If I built out the the one that we had talked about Ron, the one where we just use the collector to do this processing pipeline.
I think that that also paves the way of how we could do it in Obi as well eventually.
So maybe doing that work here isn't wasted, which is kind of what my worry is.
I know it's kind of hard to ask Nicola or Raphael. There's a lot of lot of variables in what I just said.
But I guess maybe maybe just Nicola. How did you envision taking Obi and turning it into like a collector receiver or a collector component.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 29:31 Yeah, we have an example for that. I we
don't know how we're going to do it with the collector, but we've done it with our, which is the components distribution of the collector.
**Tyler Yahn** 29:41 Right, so.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 29:44 2 things happened there is that we use the internal corrector if you will.
We created a separate interface. Essentially.
that there's an entry point into the tracer, exporter, and creation and the metrics exporter creation, that is
custom to the collector. Essentially so, the collector. When it adds a component, you take the
the additional components, I think, in the our world for the metrics. It's
look it up. Just give me a second. I don't know exactly that terminology.
**Tyler Yahn** 30:26 Yeah, I'm I'm really interested in this this interface as well, because this may be the the question.
**Rafael Roquetto** 30:32 I think one of them is the Prometheus registry from registry.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 30:37 Yeah.
**Rafael Roquetto** 30:38 Yeah.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 30:38 Yeah, Prometheus registry is one of them, and the other one is, we create the tracer
such that we directly get access to the collector, tracer, exporter, and then
generation of trees. Something I can show you the code I mean.
**Tyler Yahn** 30:56 Yeah, that. Yeah, maybe.
Yeah.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 30:59 Don't!
**Tyler Yahn** 30:59 If you want to share your screen, or I can start sharing if you want to send me. Okay.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 31:02 I'll share screen.
Oh, so let's see.
So the metrics is done through this Prometheus exporter that we have.
But that's probably less interesting. Correct.
**Tyler Yahn** 31:24 Yeah, that's yeah.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 31:25 Because we yeah, that's the metrics part. Okay? So the traces.
This is annoying me here.
**Tyler Yahn** 32:31 So is it, is it? This traces receiver thing?
Huh?
Okay, so this.
Oh, sorry you're muted. I didn't realize you're talking.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 32:47 Oh, sorry. I keep talking. I've yeah.
**Tyler Yahn** 32:51 Sorry I go ahead. Yeah. I just saw go ahead.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 32:55 Yeah. So this this traces receiver which gets passed in to to us through the interface
from the collector side.
And then this one calls the same functions that we have in Ob.
which calls this hotel generate traces. Some of the code is duplicated. They're walking on this spams, or whatever.
so essentially from the collector. When you essentially the component, you pass in this stuff.
**Tyler Yahn** 33:28 Yeah. Okay, so this looks very similar to what I was envisioning as well, like, our handler was going to implement this like traces receiver interface as well. So this looks very similar, I guess.
What is that like that provider loop that you were talking, that that's down below like? Is that
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 33:46 That's just this is, yeah.
**Tyler Yahn** 33:48 This just comes from essentially all the the telemetry that gets gets processed from Ebpf right.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 33:54 That's right. Yeah. So all the events get shipped to for us. That's in this span data structure. Request span. But in a little auto case would just be the the actual thing that you want to produce.
Yeah, yeah.
for for us, it's a little bit more complicated because we collect all the spans from different services. Right?
Saying, Think about that. There's all this
like, the 10 services, all send the data comes through this code.
And so this does a little bit more because it took to not create this massive
trace, payloads it 1st groups the spans by their resources, the trace attributes so based on the
and so on.
So you can, because of the resource attributes.
**Tyler Yahn** 34:46 Does that do batching.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 34:47 Yeah. Well, no, it doesn't do batching, it's
it it we. So let's say you have 100 spans. But there's 5 services involved
that we receive from the Ebpf side. So the Ebpf side does some level of batching, and it fills up the ring. Buffer shoots all these events over
the events come over, we convert them to the internal data structure. Some of them may be SQL. Events. Some of them are Http, we don't know
but they're for 5 different services that are instrumented.
**Tyler Yahn** 35:18 Right? So you need you need to fan those out to make different payloads for each one. Right? So what you're saying.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 35:23 So so one simplistic approach would be each
put the resource attributes for every span you create which is not a oh.
because then you're just making massive payloads right?
**Tyler Yahn** 35:37 Hundreds of them. Yeah, yeah.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 35:38 Yeah, hundreds of them. Right? So this one does group by resource, which is the service which each one has its own resource attributes.
And then it does this grouping and then shoots separated of these groups. So so it's it's.
**Tyler Yahn** 35:54 Yeah, so that's.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 35:55 Correct, but not in the sense of.
**Tyler Yahn** 35:58 Yeah, right? Yeah, exactly. Yeah. Like, it's more. Yeah, like, you're saying, like, grouping, I think is is the right term. I think I think that makes a lot of sense we cause like in the the Go auto, we actually have the opposite problem, where, like each invocation to this, like, what you have is here is this input channel. It is. It is just a single span that comes up through there, and that single span is through for a single scope. And so then.
like, what you just described is like, Okay, so you have hundreds of batches like.
we have that because we don't have hundreds of spans to try to get this grouping mechanism around.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 36:33 Yeah.
**Tyler Yahn** 36:35 So I think
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 36:37 Go orders like 1. 1 instance is one resource service, right? One to one mapping.
**Tyler Yahn** 36:43 Well, yeah. But then also, one measurement is one event.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 36:46 Okay.
**Tyler Yahn** 36:47 So so that, like each, each span comes up as a single event through the Evpf. Right buffer, right? So like it's not like it's not like the ring buffer. Approach where you have like you go and you go read a hundred at a time. It's like, No, we get. We're one to one is the is the thing here.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 37:03 I see so and so we we grab the array of event buffers from
from Ebpf we can, we all our pipelining assumes array of spans, what we call.
**Tyler Yahn** 37:17 Yeah.
So that's that's going to be interesting. Right? Because, like, I think we're going to run into. This is exactly why we want to start on this Epf program right? Because, like, we're going to kind of run into this if you try to reuse the database probe over in the ob space right? Because right now all we can do is send you one event. But, like we need to be able to do, I think, a little bit of a different structure there at that point.
Which is good. I think I think we can solve that problem. I don't think we have to solve that in this meeting. But I think that kind of answers. Your question.
ron around like whether we want to try to build out this extra pipeline. It sounds like our handler needs to
either be adopted or we need to update it to handle these like different things for different payload sizes.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 38:03 And I don't know if you guys, this makes sense to see. This is how alloy guys
connect the component. But I am not sure how many of these concepts are translatable directly into the
into the Plugin model for the collector. I would imagine it's similar. But essentially this is how they create. They have this concept of a run.
And then, yeah, so
and there's like, I guess, selector where it's done, or the config has been reloaded, or something like that.
And then through this config they pass in this Prometheus registry. That's for our metrics, and
through this config this also should receive the configure traces exporter based on the features that people selected.
So when it creates the config passes in this traces, receiver, config
**Tyler Yahn** 39:01 yeah, okay, I mean, this looks, yeah, this looks a little. I mean, it definitely looks a little different than what the collector does natively, but it doesn't look that far off.
especially like this config parsing like there's more.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 39:13 Yeah.
**Tyler Yahn** 39:14 There's tons more structure in the collector, which I don't know if it's a great. I don't know if that's a good thing. But anyways, like.
yeah, this looks similar. So, yeah.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 39:25 Yeah. So this run, Bayla component does pretty much.
not much. It just goes straight into Bela, which is now only.
**Tyler Yahn** 39:35 Yeah.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 39:35 Run. Only just go straight into the process of setting up app observability and app observability, and so on. Whatever.
**Tyler Yahn** 39:44 Yeah, I think the difference in the collector is that since they don't have like a guarantee, it's going to be Bela. It's more generic. So like this run, Bela command essentially, is like, can be registered as a component. And so then those like that that function then gets run each individually by what is what is actually registered as a component. But yeah, yeah.
so it looks. It looks very similar. And from what I've done in the prototyping of how we would get this receiver to like work like that looks the same.
So yeah, I think it's just like it's more the I think the bigger differences are on our event looping and like
what we discovered when doing this and like when Ron was prototyping. This as well, is that like we actually needed to build batching in, because otherwise we're just sending in hundreds and hundreds of payloads down through the collector that are like one span payloads.
which is which is what you've already described is not ideal and it isn't ideal. So yeah.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 40:38 Yeah.
So this is how it sets up the receiver. So they call this convert trace consumers, and they pass in the Otel collector consumer.
And that is this. I guess an array of auto collector consumer traces.
Let's see that it practically creates a config for us with these trace consumers, which is directly.
**Tyler Yahn** 41:08 Yeah, that actually looks.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 41:10 Yeah.
**Tyler Yahn** 41:10 Really similar to the collector. Yeah.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 41:12 Yeah, I mean, it is over collector. I think it's just underneath.
It's a component. It's using the ultra collector component.
So that's why I thought it was really not that hard to build. Given that. We've done this or the alloy team did this
or mark from our team radiology team did this.
**Tyler Yahn** 41:31 And so this is in the alloy code. Or right, this is, we're looking at ally code. Yeah, okay.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 41:36 Yeah, yeah.
**Tyler Yahn** 41:38 Yeah, I mean. So I think if this is
so the goal, I think, is is to get this in either the collector contrib, or into
the collector itself, as a component.
So I I mean, obviously, we can do this. It looks like it's possible. It's just how this is gonna like, look in the full integration path, I think, is kind of the question.
and then going.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 42:02 This, could you? Do? You know, if the collector can reload to config, hard reload.
**Ron Federman** 42:10 Yes, there is like an interface there. I think it's called the Config of item, something like that that's like it has a watch function.
It can. It can reload.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 42:21 Yeah. So that was the hardest part that the part that was last done that was most difficult. But now ob should be reloadable.
with the config. So what this does is reloads the bela component, which is effectively just an ob component. Now
every time a new config is launched for us. That was the main challenge was that
we had to ensure that we properly unload everything. It's not termination of the process, but it's like when the context dies of the parent and says, Shut down, done, everything should die, including all the probes, should be unloaded, and meant no statics as well.
Any static that we had had to be reworked into
an object that will go away when it reloads, because we have plenty of use with statics, and
and that just sits in memory forever until you kill the there it is.
You. Gc, the component which this wasn't doing. So yeah. So this update
gives us the new component arguments
that we then pass to a channel. And this channel does this whole thing with killing the previous
waiting for it to die and then starting the new one.
So yeah, that makes sense.
That kind of component reloads. So we don't like Ob does not support whole reload, but effectively through the
through the collector. It relaunches the component.
shuts down the previous one and restarts the next one.
**Tyler Yahn** 44:03 I see.
Huh? That's interesting. That's good to think about, I think, in the in the manager interface right now, because that was also something that Ron was looking to add was like a hot reloading to that.
So yeah, I think we need to take a look and and decide what direction we want to go there. If we want to make it simple and do something like what you're describing here, where it's just
the management process will do the the reload by restarting the process, or if we want to plumb that all the way through.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 44:35 Yeah, yeah.
**Tyler Yahn** 44:38 I mean, like, it doesn't really change.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 44:40 Yeah, we took the easy way.
**Tyler Yahn** 44:41 What? What you're what you're describing is what the manager does right? Like. It's just oh, here's all the things. Let's go up all this stuff. And yeah.
so okay, cool. Well, thanks for
showing us that I think, based on the kind of what you're not based on what you're saying, it seems kind of like what my initial thought was that I wanted to wait on this
handler
pipeline, just because it sounds like it's going to change. And I think one of the learnings is going to be this, how we're going to be sending data out of probes is going to help determine what that, what that pipeline is going to look like from the handler side.
So yeah, to answer your question, Ron, I think I still want to wait on this this initial phase, one, before we move forward on that.
**Ron Federman** 45:31 Okay.
**Tyler Yahn** 45:36 Well, cool. All right. That was a lot. Any other topics people wanted to talk about.
Okay, if not, we can end it here. Thanks everyone for joining. Appreciate seeing y'all appreciate all the hard work a lot more coming up. So yeah, we'll keep checking in on that and moving forward.
Talk to you all in a week's time. Bye.
