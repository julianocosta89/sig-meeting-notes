SIG: Collector SIG
Date: 2025-07-23
Duration: 64 minutes
Zoom Recording URL: https://zoom.us/rec/share/qeieLMPfS8oC5D1z_ZB84VUugkAqceckbM50gXj0AhrEp1PfsYgdPHv1O1Wn1O-r.h7LzZQhCm-dGEB10
============================================================

## Zoom Recording Transcript

**Pablo Baeyens** 03:19 Hey?
Should we get started.
**Dmitrii Anoshin** 04:46 Yeah. Sure.
Bye, everyone.
**Stephen Lang** 04:55 Hey? So mine's the 1st one up. Shall I just go ahead.
**Pablo Baeyens** 05:00 True.
**Stephen Lang** 05:01 Yeah. Okay, so the link that I have there for the docker receive. It was my 1st ever contribution to open telemetry.
And it kind of, you know.
has been there for quite a while. I wouldn't. Just.
I've asked around a few different places of where to maybe get a review on this. Who to talk to I got put onto this sig, so I don't know if anybody here knows who in particular I could ping about this or maybe. Yeah. Point me in the right direction of another sig or select channel.
Please, cause I'm happy to do the work. It's just I have some kind of questions.
Okay, yeah, do both of my topics? Sure.
**Pablo Baeyens** 05:56 Have you spoken with the semantic convention, Sig? And specifically the Kubernetes? One.
**Stephen Lang** 06:04 So I was just there.
but they tend to just mostly talk about K. Eights stuff. I wasn't sure whether just to bring it up there. Are you thinking?
Because it's containerized? I should bring it up in the K. 8 Sig. Instead.
**Dmitrii Anoshin** 06:22 Yeah, I believe that's it.
**Pablo Baeyens** 06:23 So.
**Dmitrii Anoshin** 06:24 More containers and Kubernetes in general.
**Stephen Lang** 06:27 Okay, it's a shame. I just just out of that meeting.
**Pablo Baeyens** 06:34 And I would also think it's a good idea that you check with them whether these where are they finished developing these conventions or there's still changes that need to happen, because if there's still changes that need to happen, then well, we may want to wait until they are finished, so that we don't break our users twice.
**Stephen Lang** 07:01 Yeah, that makes sense.
Okay, yeah, I'll pick it up with them next time around. Then, thank you.
**Pablo Baeyens** 07:09 Okay. Sorry that the ordering wasn't the right one.
**Stephen Lang** 07:13 That's all good.
I'll continue trying.
Yeah. So that's someone suggested. I do both topics. So the other one again, I'm just looking for. If this is the right sig or not, but from the Kubernetes sig Tyler over there was asking who might look at the open telemetry helm charts, because I think the looking to to get this merged in. And it's it's been a couple of weeks since there was feedback again. Is there like a slack channel, or another sig like well, or who do we talk to about the elm chart side of things.
**Dmitrii Anoshin** 08:02 We have a channel called Hotel Help.
You can ask there in Cncf. Slack.
**Stephen Lang** 08:10 Okay.
**Dmitrii Anoshin** 08:12 So they just want to bring the Pr that is being is.
that is not being merged right.
**Stephen Lang** 08:23 Yeah.
Yeah. Well, I think it was. It was mainly looking for a point of contact on on that to you know, for kind of ongoing questions, for, like, you know, future really.
**Dmitrii Anoshin** 08:33 Yeah. Slack is a good place to put that, but they believe, like the direct comments from Tyler that are still have hasn't haven't been addressed.
**Stephen Lang** 08:43 Sure.
**Dmitrii Anoshin** 08:43 So it's not like.
There is no reply from the community on on that issue.
**Stephen Lang** 08:51 Yeah, no, I think the the question was just in general, you know.
if there was another avenue outside of Github. But yeah, I'll check out that slack channel and pass that on. Thank you.
**Dmitrii Anoshin** 09:00 Sure.
**Stephen Lang** 09:02 That's it from me. Thanks.
**João Duarte** 09:10 Yeah, I'll go next.
Yeah. So I'm I'm I'm sure I'm not supposed. I'm not sure if we're supposed to like introduce ourselves. But it's the 1st time that I'm speaking at the at the Sig. yeah. So I I work at elastic and and mainly in the locks dash project. And one thing we do is we're encouraging more and more usage of the collector, obviously. And and one of the limitations that we're we're seeing when wanting to migrate is around enrichment, enrichment, capabilities.
So I wanted to kind of bring this to discussion, mainly trying to understand the interest of the community and to grow the enrichment capabilities of the collector.
I've seen some issues on it in contribut and overall. I'm trying to look for strong opinions in this group, either like strong feelings against it, and we can talk about that or strong feelings towards it, and we can do collaboration on it.
That said, I understand that for opinions to be formed we kind of need to understand what we're talking about here in terms of enrichment. A very vague concept same thing with with lookups. So I wrote the document that is in the in, the.
in the document for the the meeting. And yeah. So the goal is to kind of talk about what kinds of enrichments exist. What kinds are supported today by the collector? What kinds are supported by other tools that play in the same space as the collector. And yeah, which ones should we add to the collector? Or should we not add to the collector, and it also finishes up with like a draft of a proposal. Because I kind of wanted to 1st introduce this topic here before. It's just immediately creating a proposal as an issue.
and yeah, I'm I'm not sure what next, either. I can either go through the documents 5, 10 min, or just collect feedback after the meeting throughout the week.
I don't know whichever is typically then our preferred year.
**Dmitrii Anoshin** 11:20 I would just ask one question about the document.
If it does okay the cross event correlation. What what you want to achieve with that. Speak like keeping open telemetry concepts in mind. How would you? What what would you see as a result.
**João Duarte** 11:42 So the the goal of defining the types was not necessarily to say, Okay, this definitely belongs in the collector. It's more of a here's what all of the data collectors out there and data transformers are doing.
Some of them are most focused on logs, and therefore, like they need to correlate a log from this type into another and generate a 3rd log entry or or events based on on 2 log entries.
so it definitely depends. It's definitely more common on logging signal versus metrics and traces that said, it's up for debate. If there are, use cases in the collector to do it. And if not, let's leave that whole category aside. And let's focus on others.
Mainly that document talks about that.
We could add more around static and dynamic lookups as as the type 2 and type 3 of that document.
And that's kind of the the ones that I I see more need. And I also see the need for that in the the issues that have been created, either like a few years ago in contribut, and also a couple of them in the last 2 weeks, 3 weeks.
**Dmitrii Anoshin** 12:51 Sure.
I believe that that problem is just like over overall open telemetry problem, not specific to the collector and collector. Oh, sorry. Open telemetry originally was started with that correlation as a requirement. That's why we have semantic conventions where, like all the like, let's say, attribute names, and everything is defined for all the signals, and also, like, as you mentioned, locks and trace correlation. I believe it's library work. So correlation needs like the best source for the correlation is is actual source of the producing the data. And so that problem is associated with the instrumentation. And I believe it's been solved. Like, I mean? I'm not. I'm not know, don't know the state, but I believe it's like when you instruments and some put its log logs and tracing and instrumentation it will.
all the data will be correlated with trace Id for particular logs. I believe so. I'm not sure. I'm just saying that I'm not sure what additionally, can be done in the collector to help with that particular enrichment type.
**João Duarte** 14:09 Yeah, for fair point. I mean, I I could talk about that in in previous work I was working at a telco, and we had a bunch of like network devices. And and we just had to receive data through Tcp sockets and then come up with correlations because they they are part of the same like Dsl and Iptv stacks. And then.
there's no like instrumentation you just have to like. Say, Okay, I know that this field has the id of the customer. And it's that other field in that other network device I kinda need to correlate those to signal that the whole stack is not working. For example.
**Dmitrii Anoshin** 14:44 Yeah, I see. Yeah, the idea of open climate would be that that data, when when it where it originates, it would produce telemetry, which is already have correlation in place instead of collector figuring out.
But that's like that's ideal world, right? Maybe it's not as you, as you said, for for this networking devices. Maybe it's not realistically visible short term.
So maybe.
**João Duarte** 15:13 Good. Point, yeah.
**Dmitrii Anoshin** 15:16 Yeah, I got. I got the the idea. I think.
**João Duarte** 15:19 Yeah, about to comment around Wi-fi definitely, it was just yeah. I added a few tools. I can add an extra one for sure, and if anything's wrong in terms of the what existing tools versus the other, please please let me know. This was just a try to to represent every tool unbiased jay like I mentioned, I can either go through it. I know that we have a lot of topics today. Maybe we can get feedback Async.
**Dmitrii Anoshin** 15:58 Yeah, probably we. We can take it offline again.
encourage people just to take a look and comment, if possible.
**João Duarte** 16:06 Yeah, at the end. There's already a draft for a proposal with all the fields populated. So yeah.
welcome.
**Dmitrii Anoshin** 16:14 Do you have an issue somewhere in the collector regarding this thing?
**João Duarte** 16:18 So not yet. That was my I'm I was not sure how to approach this. It was like, I didn't want to create an issue, and then immediately say, like, we don't even want enrichment in the collector at all. So I kind of wanted to have this as a baseline for discussion around terminology and what to do. If if it's better, I can just create, for example, the draft proposal that I have there as an issue.
**Dmitrii Anoshin** 16:39 It's not a proposal, probably issue just for discussion. Right? So there is a for too easy to discover this this. Like document, right? Because otherwise, only people who are on this call know about this one. But if you create an issue, it's gonna be official, at least to bring people more, more people for the discussion.
**Pablo Baeyens** 17:05 Yeah. And, as I just said, on the on the Zoom chat feel free to also share this on auto collector, dev on slack, because that's another place where a lot of collector contributors are around.
**João Duarte** 17:18 Yeah, I'll do that. Then I'll pass the the data into an issue and then spreading chevron.
Thank you.
**Dmitrii Anoshin** 17:42 And the next item is from Victoria.
**Andrzej Stencel** 17:50 Victoria's not here, apparently.
**Dmitrii Anoshin** 17:52 Okay.
So maybe we can go to the next one. Josh.
**Pablo Baeyens** 18:00 I mean I I can maybe mention what Victoria said. So.
**Dmitrii Anoshin** 18:06 Okay.
**Pablo Baeyens** 18:07 She's creating this year's auto collector survey. The questions are similar, ish to the ones that we did on the last collector survey.
I don't know.
Do do people have access to the The form linked the 1st link on on Victoria's bullet point.
**Andrzej Stencel** 18:33 Nope.
**Pablo Baeyens** 18:36 Okay?
So yeah, you should DM her, then to get access just you should be able to access the the slack thread, the second link. So just if you're interested, just say so on the slack thread on you can.
You can get access from here.
Give feedback on the questions.
so we can move on to Josh.
**jmacdonald** 19:26 Hi, everybody so this is just a quick placement of an idea that has been talked about. And I'm bringing my 1st draft to the group here. So A few months ago, we announced and worked with the Hotel Governance Committee to get this hotel arrow project up off the ground. We we said we wanted to do rust components, and we said we wanted the collector to support them.
And we were so so this has been evolving a bit. We we're really trying not to to say rust collector. We don't want to break this or community like, so we're we're trying to figure out how we can use rust code in a go collector which is not the easiest thing to do in the world. But, there's lots of our prior art out there and I've done some research on it. So this pull request here I pulled it out of draft so that people would see it looking real. It is pretty high level. I laid out 7 steps.
Try and like isolate the work into sort of smaller pieces and I I and thank thank you, Pablo, for putting a few initial questions on there. So I've tried to. I've given my own answers for those initial questions.
in the issue or in the in the pull request.
Let's see. What do I want to say? you know. I understand that that see go enabled is one is a pretty big deal here, and we wanna make sure that we that we don't suddenly confuse the build and make it harder than it already is. So we definitely need to Co continue supporting pure. Go and there's a there's a section in the plan. Actually, that that addresses the topic of how would you run rust components if you're required to use pure go and of course we know how to connect collectors together, and so if you have an Otlp receiver and exporter, you should be able to do that using a sub process so we talk about actually supporting sub process. Mode, which is, you know, requires essentially transforming a configuration that was once a single processor and turning it into 2 configurations.
with additional otlp, exporters and receivers, and so on to bridge the 2 together. So by the end of this stage phase, 6 includes this subprocess mode as a fallback that I was just describing, and then phase 7, which is, I admit, very speculative. But the the employer who sent me here definitely would like to get us to have plugins eventually so the long run goal here is to is to be able to separately compile.
not just rust components, but go components as well. And again, we've done the research. It's not gonna be easy. But this is a proposal that might work. So I want to sort of publicize this and share it out. It's pretty much brand new, and I'd be glad to talk about this formally or informally, anywhere on slack. We could have a zoom. If you want talk, talk about this one on one. If this concerns your interest to And yeah, I think I'm gonna leave it there. If there's any comments right now, I'd be glad to have QA.
**Kells** 22:38 So maybe just ask the silly question here. I I really like the idea of the the arrow protocol being used. And is that so? That's not actually possible to install on kind of the native client right now, right.
**jmacdonald** 22:52 yeah, let me let me try to address what I think you're asking. Because this is not a new topic. Okay, so When we began the Hotel Arrow Project, which was 3 or 4 years ago now, we, we began saying the roughly. The same thing, as we're saying now. And at that moment, in time the this collector was quite a lot less mature, and we were asked at that point in time just to work and go and it, you know, we did. So. That was, that's how we ended up having the hotel arrow components in contrib and so so what those components do is they receive the P data, or they they they send and they consume and produce P data objects, and but on the wire between collectors they use Grpc streaming, and they use arrow ipc, which is a library for compressing and transporting column oriented data.
So our components from the phase one of Otel just dealt in P data and did compression on the network. And for this phase, 2 of the effort. What we're really trying to do is is go the other direction and focus on on inside of a collector. When when you, instead of having a P data that is represented as an Otlp, essentially an Otlp protobuf object. That we would. We would have what we're calling P data being backed by the arrow record batch. So instead of having protobuff data, you would have arrow data.
and when we came to phase 2 and saying, Okay, now, we're really serious. We want, we definitely want Russ. We're trying to get to data fusion. We're trying to get to some of these high high powered engines that are out there.
And so our argument was, we we've been asking to use rust this whole time, and now we're now we're here. We want to be able to use rust because there's irreplaceable code in the rust ecosystem for arrow and data fusion, and so on. But the getting back to the question that was asked. Nothing that I've said precludes us from doing arrow as P. Data in go.
The problem there is that the arrow ecosystem is way less mature and go it exists. We use it, and you know the the arrow go. Arrow libraries are present, and being used in those arrow exporters and receiver components that we did. But the the number, the volume of contributions, the size of like just the whole ecosystem is much, much smaller.
doesn't mean you can't do it, but it means that the cost benefit might be different, you know, working in with arrow record batches in go is going to have some resistance or some sort of friction there, just because you go to a lot of trouble to get into the arrow environment. And then what? What do you have and go? There's not a lot of work that you can do. Not like query engines and go for arrow. Mostly you're using arrow to get in and out of another runtime and go frankly. So.
and I may have oversimplified and over generalized. But What I'm trying to say quickly is that we can implement arrow in in the Go environment, we can have P data be represent backed by arrow data batch record batches as well.
It means essentially having a completely separate pipeline and you can imagine converting between the Arrow and the P. Data and the Otlp representations. Those would be standard conversions, and and that's the thing that the Hotel Arrow Project is getting good at. So we know how to convert between Otlp and Otto Arrow and back again. So we can definitely imagine having a go collector that does Arrow. I'm just not sure that their benefits are there for us.
again, not a new idea you could imagine having p traces and p traces be either otlp or arrow. Yeah. So so at 1 point it was proposed to have instead of p traces, you could have a traces or something like that, just a separate data type and separate pipelines with explicit conversions between them. I'm going to stop talking, Braden, would you like to big.
**Braydon Kains** 26:53 Sure. I maybe I misheard.
or I'm simply confused by reading through the issue when you're referring to a like a plugin and go. Are you talking about like there's like a dl open like a runtime loading of a plugin or.
**jmacdonald** 27:18 That's that's the intent. Yeah, and those of us familiar with the go compiler, tool chain and runtime know that that it's a weekly supported. There is a plugin package and go, and if you're not on windows it may work for you. It has a million restrictions which are, are real. But, like I liked the the earlier speaker, Stevens, gave us a document with a matrix of different collectors and feature matrix right? Most of those other collectors do plugins. And I. And I think that's pretty important.
Those other, the ones that are working and go are actually using the go plug in environment which doesn't always work. And that's why I pre-produce this fallback plan to make sure that even when the plugin, the deal open or whatever doesn't work. We could still combine these pipelines.
**Braydon Kains** 28:08 So so this is like the go plug in ecosystem, and not like see go like calling systems. Dl, open.
**jmacdonald** 28:17 Both of those realities exist in my proposal so to to work with rust, you're gonna if there were a rust shared library, it would be a deal open.
And it's and it's and a foreign function, interface and standard C library, dl, open stuff, Dl, SIM and everything. If it's a go Plugin. You gotta use the the plugin package from the go, the go compiler, tool chain.
and yes, I've done quite a bit of investigation to see that you know what's possible here. Shared libraries are hard. That's definitely why I put it in phase 7. It's the end of the line. If this can't happen, I would. I would still work on phase, you know, steps one through 6, and I would give up on plugins.
Pablo.
**Pablo Baeyens** 29:06 Yeah. So I think it's great that you're working on this. I think there's probably going to be a lot of discussion about a lot of the fine grain points here.
I wonder if we need to start smaller and just like just solving the the Seago story on like, are we going to have Sigo enable set to 0 by default?
are we going to allow it just for components that use raster in general like that kind of thing just by itself seems like an Rfc. To me. So I don't know. I my comment. Maybe it's like we probably need to start smaller than this.
**jmacdonald** 29:57 I accept. Yeah, I mean, I think the little most of what I'm describing requires you to use Sigo to to do the foreign functions into and out of rust.
but I agree that that the there's got to be a hard requirement from the beginning that there, you know, Seago, it doesn't have to be enabled. And and you can continue using this code without Seago. I 1 of the ideas, Pablo I had, I think is that there's there's a concern here that there's just like a lot of experimental and risk in this proposal, and we don't want to begin it. If if it's going to be too complicated, or break the build, or, you know, ruin the Seago, and you know the the no Seago story.
I I do think that prototyping further into this plan and showing what it really looks like when when you implemented, you know at least half of this stuff before going anywhere would be a sensible approach. And I am probably gonna propose I'd like your approvals on this to use a fork of the collector which we actually made a fork years ago, for the same reason. That would let us at least sort of begin these experiments, showing what it look, what would look like in the actual collector, but not modifying the actual collector. That's going to be my proposal.
Dimitri.
**Dmitrii Anoshin** 31:27 Yeah. My question is, if we have to use rust for hotel error, does it mean that we would have to reimplement potentially every company to be able to use with error. In that case, reimplement it with rust, and maintain 2 different versions.
**jmacdonald** 31:47 The the way this proposal looks today, the Otlp receiver exporter, and and the equivalent otap we call it the Otel Arrow receiver exporter.
those would be reimplemented.
because we believe that Otlp is a sort of standard feature for these pipelines, and that's the way we would get in and out of rust if we had to fall back to the sub process. And I think the practical configuration that is interesting to me. When you do mix these. I think there are definitely purists out there who are like Josh, stop talking about mixing these. I just want a rust pipeline, or I just want to go pipeline but but just like I mentioned data fusion like, you're never going to rewrite that and go.
Prometheus is never going to be rewritten in rust. It's going to be a go code base forever. It's big, it's complicated. You can't rewrite it. So if I want Prometheus, it's got to be a go receiver if I want to. Then, you know, use a data fusion, pipeline I have to get out of. Go into rust at this point. If all I want to do is export Otlp, it would be better to just use the rust exporter than to go back into. Go to use the Otlp exporter, because Otlp exporter is trivial, and we should be able to do that in both languages.
But but so the goal of this is that we don't want to rewrite. You know the the actual components other than those built-ins like Otlp.
**Dmitrii Anoshin** 33:13 I mean, my my point is that if we have any other comp components in the pipeline, it would like it would require translation to regular otlp right, and to rust and go rust.
Does it really make it more efficient? In that case, so it'll it'll make it more efficient, and to work with error only if you have Otlp receiver and Otlp exporter, and nothing else in the pipeline. Is that true?
**jmacdonald** 33:44 Well, the the objective that we have is because, you know, data fusion opens up like a whole world. We think of query opportunities here. So you know, I want to get into a data fusion processor, mainly and I think that that opens up the possibility to do more with persistent store to do more more like long term storage, for example, because of the powers of the this data fusion library.
but I but but you know we don't want to lose the benefit of of the long tail of so many components. And so I think the the belief we have is that there will be components where performance is very important, you know, due to the volume of data that you're potentially using. And there'll be components where it's not so important, and it would be, you know, simpler to just leave them and go. So if there's a high throughput demanding data data pipeline, it may be better to rewrite something in one of the languages to make this better.
I hope I've answered your question. I guess the idea is to provide Otlp export and receiver support so that you never have to cross a language boundary just to get to an Otlp service. I hope that helps.
**Dmitrii Anoshin** 35:00 Okay.
Thank you.
**jmacdonald** 35:03 Rayden.
**Braydon Kains** 35:05 Just another quick clarification that we. So we're talking about Seago in that in that final phase. But is that like we, we might make another collector distribution and releases that is built with Sigo to allow for this functionality. Are we wanting this, like in the main artifacts that we produce.
**jmacdonald** 35:26 Hadn't thought through that. Actually, I I don't want to disrupt the current release releases. So I think it might be. You know, we could make make a new release artifact. That's like the the Seago enabled experimental collector that we've got the part part of this plan, and and the main difficulty in plugins for the record. This phase 7 of this idea, is that that both in rust and in go like you have this very strict requirement to have exactly matching dependencies means you can't really hot upgrade any of this stuff. You gotta like.
PIN down every one of your dependencies. Build the collector core and then build your collector plugins with the same exact dependencies. The solution that I imagine for this is to somehow seal with like a Hermetic build environment. So here's a docker container that contains, like the entire set of dependencies and can build you plugins.
So I would imagine, distributing both the container for building as well as the artifact, that you need to run the the plugins as well. But this can all. I think this. These are very long for further out questions.
**Braydon Kains** 36:35 Yeah. So I like, I, we, I have some experience with this that we like. We distribute 2 collectors, one of which is built with Seago to allow for. Like Gpu receivers, we have to like dynamically open and video libraries and stuff. And like the reason we haven't just like thrown those Gpu receivers upstream is largely because, like Sigo, is incredibly disruptive to releases to packaging because you're relying on a glib c or any other dynamic dependencies on the system. So all of a sudden this pattern of like contriv has one dev and one rpm, because all it is is a binary like that's broken, and all of a sudden you need to now build and link on all the distros you want to support. And that's why I figured Seago was never making it into like normal contrive. And that's so. I I'm interested in in seeing like this can of worms reopened, I guess, because I kind of figured that was sealed.
**jmacdonald** 37:29 Great. Well, I'm really excited that you have some experience, and I can ask for help like maybe I could ask you for help, because I don't really know exactly what I'm the can of worms. Looks like. I just want to open it again, too.
**Braydon Kains** 37:39 Yeah, I I'm I'm thinking very deeply about all this stuff right now. So if you want to talk, see? Go.
**jmacdonald** 37:43 That'd be great or anything. Yeah.
And I actually, the Gpu thing sounds neat. Can you tell us what the receiver would do for us if we had it.
**Braydon Kains** 37:51 So we have 2 receivers. One is for Nvml, the Nvidia Management Library, and the other one is for Dcgm, the data center Gpu management. There is a Dcgm. Exporter that Nvidia maintains, for, like a Prometheus, one but our like, we think our design for the metrics is a bit better. And we have a product called the Ops agent, the Google Cloud Ops agent, which you can look up to see the Gpu metric experiences that we've built around those receivers, and so like when you install like a Gce deep learning image, and it has the Nvidia libraries on it. You throw the Ops agent on there, and it automatically will see. Like, okay, you've got Gpus. Here are your in context, dashboards and stuff from the metrics that we've pulled, using those libraries. But to use the bindings from Nvidia it is largely required that that you have, Sigo. So you can Dl open the live Nvidia stuff.
and I've tried as an alternative I've explored using a library called Pure go, which provides Dl open without see? Go, but it is. It is ugly and scary to put in production. So I kind of stop short on that. But I'm happy to like open like, show you what I what I found and and talk it over.
**jmacdonald** 39:11 8.
Yeah. I had a coding agent tearing apart the go tool chain at 1 point, trying to figure out what would it take it's like some of the stuff in Plugin is almost supports what we want to do. And anyway thank you. I'd be glad to talk with this about this offline. Appreciate your help.
**Braydon Kains** 39:27 Yes.
**jmacdonald** 39:28 Andre, would you like to speak.
**Andrzej Stencel** 39:30 Yeah, maybe just quickly. I'm trying to understand. Like how it's supposed to work. Sorry if that's already answered in the whole, maybe piggybacking on what Mitri was asking. If I if I want to use the Hotel arrow receiver, maybe do some processing with an existing rust processor. But I also want to use the transform processor. I need this to be implemented in rust.
**jmacdonald** 40:01 I would give you 2 answers. So so let's suppose you start with a rust receiver, for whatever reason, and you go through data fusion or some sort of like custom thing. For whatever reason. Now, you also want to transform in in, go.
okay, so we're gonna build the basic mechanism. Then to cross the the Runtime boundary. It it won't be free. And in the on the, on the rust arrow side what we're doing is working on like super optimized routines to go directly from the record batch to the bytes. We don't want to have to construct an intermediate protobuf object, for example. So we're trying to make it very fast to get to and from the bytes of a protobuff as the interchange mechanism.
So it'll be fast, but it still won't be free. So then, so so yes, you'll you'll, you'll imagine, coming through a rust pipeline, a rust receiver, a rust processor, and then now we see a go processor.
If it's in one environment, then you're you're gonna serialize to a shared piece of memory and then invoke the Ffi, and then you're going to deserialize from that same piece of memory, and then you can process it with the transform processor. Now you're in still in the go, pipeline context, what's your exporter going to be ideally?
If it was a just an Otlp exporter, you choose the go exporter because you're in the go runtime at that point. If I had, I hadn't run the transform processor, I would choose the rust otlp exporter because it's cheaper, and there's no feature in the otlp exporter. It's just a like specified translation and export.
**Andrzej Stencel** 41:31 Let's say I want to export in Arrow as well, probably best to go back to rust.
Well, but we do have.
So there. There are 2 types of translations that we're talking about between Rast and Go, and between the backing structure of the P data, whether it's arrow backed or regular protobuf right.
Okay. Okay.
**jmacdonald** 41:57 Okay, thanks. Yeah.
this this is gonna run into a time time box. And I would be glad to have more conversation later on. This as well. you know. There there is. There is the Go Hotel Arrow exporter. We don't. We don't want to discontinue that either, like if if.
But the the fact is, you're dealing with P. Data. Otlp objects right now, and the Otlp export is, you know, got to do a bunch of manipulation, a bunch of object transformation. Whether it would be cheaper to do it and go or rest at that point I don't know. But we should definitely the goal is to avoid unnecessary conversions.
Braden, will you please?
Oh, sorry you had your hands up. I I think we should.
**Braydon Kains** 42:43 Sorry. I sorry I I was muted. I'll make it quick, but it's it is somewhere related to the joke about awesome, too.
You mentioned that to cross the boundary you're making a shared space of memory, that the Plugin is going to load and serialize from who is in charge of keeping that memory managed.
**jmacdonald** 43:06 I looked at this rust to go library. It's linked in my proposal. It's from by dance. It involves a bidirectional ffi to do memory management. That's the short story there. If it doesn't work, it doesn't work, but it looks pretty appealing to me.
And it essentially addresses the the question that you just gave.
**Braydon Kains** 43:27 Okay, I'll look into that. Because in my wasom experience experiments like that crossing the boundary like, how how do you, who is in charge of the memory is by far the the biggest and the reason I the thing I could not overcome.
**jmacdonald** 43:41 Well, okay. So I since we've now the topic of Wasson has come out. I wanna say that this is something we're all. I think everyone here would be be excited if we could ditch the like rust story and just do Wasson.
actually, I mean. And and I know that go can compile to awesome. And I and I'm I know that Russ can compile to awesome. So I will say this much before we, I think, need to move on.
The collaboration with hotel Arrow has always involved myself. But but F. 5 has been involved in this for a long time. And Laurent is so F. 5 is a big wasom shop. They they would love it if we were talking about Wasam. I just you know I come back to how Prometheus is written and go, and I don't think it's going to be compiled to Wassom anytime soon, and that's pretty important for me. So to have pronetheus, so I think we have to approach the go, and the rust interrupt without talking about Wassum. But I think Wassum would be the best solution we can come to in the end.
**Pablo Baeyens** 44:45 I think we have everything else in Wasm but the Prometheus arts and go. That's fine. But yeah, I don't know, like we don't need to be super ambitious and have everything in Wasm.
**jmacdonald** 44:56 So so everybody keep keep your their eyes on Lawson. I think that's gonna be interesting. But I'm not an expert on that.
**Braydon Kains** 45:04 If if there's time after I can talk a bit about what I did. But we have more topics on the agenda, so we can.
Okay.
**jmacdonald** 45:09 Thank you. I think we should hold that off and continue next time.
I want to yield to Cindy.
**Sindy Li** 45:16 Yes, yeah, let me keep this break brief. So I'm trying to come up with a solution to propagate context across batching. So during batching multiple requests and their attached context are merged into one piece, and we have the logic to merge the P data already. But it's not as intuitive what exactly it means to merge context.
The use cases that I'm observing would be, for example, interceptors that's outside of inter open telemetry like a Http interceptor that has access to Http request and context.
But it doesn't necessarily have access to open telemetry data like pdata or request, and they might have some metadata, for example, tokens or user id that are stored in the context. I haven't been a heavy user of context or golan. So I'm looking for some eyes from Golan or context expert. I have the the issue kind of contains some proposals, and there's also a draft that implements the idea. And I would appreciate some eyes from Golan experts. That's mainly the topic.
Cool. If there's I'll I'll hand over back to Joshn.
**jmacdonald** 47:10 Thank you. Thank you. I'd like to help with the context. I'll take a look.
Okay, so this is actually me speaking for a coworker of mine. If you see the issue that I just filed, it's about adding new metrics. There's a Pr that's been open for like almost 2 months. And I I started asking, Why is this not merged yet? And the reason was that everyone was a little bit afraid that all the Maintainers were a little bit afraid that it was going to add some new cost for users and vendors that weren't ready for it. And it was, I sort of quickly responded. I don't think we want this to be on by default, or we didn't expect it to be, and there was a question about whether this enabled flag in the Metadata Yaml works. I found this issue basically to say, we think that the best default for introducing new metrics would be to turn them on as detailed meaning they shouldn't be on enabled by default. That's the simple thing that we're trying to say. We're not sure that that feature is tested or that it works. And I'm gonna make sure it is tested and works.
So the basically, the issue is saying that we intend to make sure that it's safe to add new metrics if they're off by default. This is how we'll do it. Any comments.
**Dmitrii Anoshin** 48:21 Yeah, that makes sense to me the thing that we have a document for scraping metrics. When you add a scraping metric, it says that adding metric enabled by default in a scraper. It means that it's breaking change, and it has to be disabled by default when you edit, and for scraping metrics. Metadata provides, enabled flag. But we don't have that for internal telemetry of the collector for internal telemetry of the collector we only have the levels detailed and basic whatever. So yeah, I I ideally, I think, enabled, can be added. It will be 3rd option to disable enable internal telemetry.
**jmacdonald** 49:01 I'm a little confused. Could you find that issue or that that document for us? Maybe, and put in the issue? And we can work on this offline.
Yeah, understand what a scraper metric is as opposed to an internal metric.
**Dmitrii Anoshin** 49:13 Yeah, scraping metrics is actually like metrics that are emitted by the scraper. And it it goes to actual pipeline, but not not as a telemetry pipeline, or the internal collector.
**jmacdonald** 49:24 I see.
**Dmitrii Anoshin** 49:26 So like host metrics, receiver, even Prometheus, receiver, etc. But Prometheus receiver doesn't predefine set of metrics. So yeah, I think that makes sense. What you said. We, just whenever new metrics decided it should be under a detailed flag.
**jmacdonald** 49:44 Okay, I will take this myself. Thank you very much. I yield to the next speaker.
John.
**Jade Guiton** 49:52 Yeah, I just wanted to say that document about scraping receivers is what antoine was referring to in the slack thread. I'm not sure what people think, but my, my intuition would be that there should be a difference between the stability of output we expect out of this receiver versus the stability of the internal telemetry of the collector especially because the collector is very modular. You can add and remove components that will produce different telemetry. So I'm not certain if it really makes sense to apply the same standards.
Obviously this is just my lone opinion. But I'm not sure I really understand the the implications, I guess, of adding new metric to internal telemetry, and what impact it might have also. But I guess for the record. I I think the main reason why it wasn't merged for a long time is because The pr wasn't fully finished, and there was a bit of a hiatus on working on it.
Yeah, but.
**jmacdonald** 50:59 Yeah, I I don't wanna point fingers. I actually think I was calling. It's a week approval problem. Sort of everyone said, Yeah, this looks okay, but nobody was willing to merge it, because it there was something in the back of everyone's head thinking there's something, maybe a little bit wrong with this, and I think that what I'm pushing on here is like, what like we like. How can we get out of this week? Approval, state, and and strongly believe this is okay.
**Jade Guiton** 51:22 Actually, I think I'm thinking of another Pr. Sorry. Ignore my last comment.
**jmacdonald** 51:28 I think we're good here. I think we can move on to Pablo.
**Jade Guiton** 51:33 He had to leave, I believe.
Here, yeah, he said. He said we could get yeah.
so I guess I would be next it's so there's a a Pr, let me see.
So there's this Pr on the Docs website, which is about which kind of changes a lot of things about how we suggest people do collect the internal telemetry of the collector.
and someone pointed out that.
Well, someone argued that we should suggest people do not send the collector's internal telemetry directly to an observability back end. Instead, they should send it to what I think is a description of a gateway layer to avoid having issues with too many collectors, sending the telemetry to the same endpoint.
and I don't have that much experience with deploying a bunch of collectors in a production environment. So I wanted to ask the opinion of on the meeting.
Does it make sense to recommend against sending collect the collector's telemetry directly to the backend and insert a command.
Sending it to one central collector in your infra that then emits it out.
**Dmitrii Anoshin** 53:08 I'm not sure why we're talking about open telemetry, collector internal telemetry. It's like all the data that collector sends. It's pretty much the same right.
I believe if you send. If you have huge fleet of the collectors, it'll be much more connections, and you would get small batches. So just for efficiency. And like.
I would say, resiliency, we typically recommend sending everything through the collector, if I don't know, like, if the fleet is more than like 100, for example, something like that so bigger the fleet, the you should rather use gateway and the small small. This the fleet of the collectors. It doesn't make sense to use the gateway. That much.
That's what we've we've been recommending from the beginning. Essentially.
**Jade Guiton** 54:04 We're talking about a fleet of applications or fleet of collectors here.
**Dmitrii Anoshin** 54:07 Yeah, I would say I would call it agents. For example, if it's Kubernetes demand sets.
**Jade Guiton** 54:13 Okay?
So yeah, you you think that it's a matter of scale, essentially.
**Dmitrii Anoshin** 54:20 And also on the gateway. You can like add more memory, set up bigger queues, maybe add some persistance layer, so it also would guard you against some like flaginess from the back end.
**Jade Guiton** 54:39 Okay, I just wanted to. Yeah, to validate my my understanding of when a gateway would be something one to recommend.
**Dmitrii Anoshin** 54:49 Doesn't doesn't depend on type of the telemetry. It's just all the data that we sent from the collect.
**Jade Guiton** 54:55 Yeah, yeah, it's just that this is a page about the collectors, internal telemetry. But yeah, I agree that it makes sense to apply the same logic to all the telemetry in your infra Andre.
**Andrzej Stencel** 55:06 So, looking at what this Pr. Tries to be doing, so it tries to advise against ingesting the collector's telemetry into back into the collector. I think we can all agree that this is something we want to advise for, and I don't think that discussing whether a gateway collector is needed here, or should be recommended. I don't think it should be part of this. Pr.
so I think ideally, Adriana. Maybe we could drop that little part about recommending gateway or not, and just focus on the fact that ideally the collector does not ingest its own internal telemetry, and I can put a comment there.
That was.
**Jade Guiton** 55:48 So I think the the current version of the page already already does not recommend this. Like, we specifically removed the part about the collector ingesting its own telemetry.
It was kind of added back into the Pr. And then I said we should remove it, but I think the the main goal of the Pr. Was.
It's not entirely clear what the main goal was, but I think it was.
I don't know to clarify. I guess some of the different approaches for exporting the the metrics.
But yeah, I don't think that the goal was to recommend against self ingestion. I think there was already warned against.
**Andrzej Stencel** 56:32 The part of the description of the pull request, like the second sentence, is like, it also advises against self ingesting.
and I can see that wording in the.
**Jade Guiton** 56:44 Yeah, yeah, it. Yeah. I guess what we in the way before, in the old version of the page, we had a description of how to do this, and a warning not to do it. Then we removed it.
and then this Pr. Reintroduced both, and I said we should not recommend a setup, but they still kept the warning.
But I'm I'm not sure that was the main goal of the Pr.
**Andrzej Stencel** 57:11 Right? Okay, thanks. Thanks for the context.
**Jade Guiton** 57:14 It's a bit confusing, like there's been multiple Prs trying to reintroduce the concept of self ingestion on the page. Maybe we should have a more clear guideline about when to recommend that Braden.
**Braydon Kains** 57:32 My question is about what we like the the scenario that I think some people might run into, and maybe for context, that Gcp. Customers run into is like what like you can't export directly to an Otlp back end and that is a case where you do need a gateway collector if you don't want to.
So the idea of like recommending a gateway collector in this page probably does still belong here for that scenario, for the scalability thing like what Demetri mentioned like. Maybe if we had another page that explained when you should use a gateway collector like why you should aggregate at the edge or under what scenarios, then you could link out to that. But I think it it so. I don't know if we want to like fully remove this. But we should maybe like keep, because this is still relevant to internal telemetry of like, we think you as a user should collect internal telemetry. But if you're in a scenario where you can't just send direct Otlp to a back end here, you would use another collector to aggregate this stuff, I think that is probably a more useful summary. And may I think I'll just comment that on the Pr. Unless anybody thinks I shouldn't. But I will probably just comment that on the VR.
**Jade Guiton** 58:46 Yeah, I think that's roughly in line with what I with what I commented on the thread, which is that there are definitely some use cases for a gateway outside of just scalability. So like enriching the telemetry, for example, with Kubernetes
**Braydon Kains** 58:59 Yeah.
**Jade Guiton** 58:59 Attributes processor. But yeah, that's a that's a good point, like sometimes you can't export directly to the back end you want with Otlp. So that's a i guess that's another use case we can mention.
There are no more comments about this topic. Does anyone have an impromptu topic to end the call with.
**Dmitrii Anoshin** 59:42 Think we can wrap it up. Thank you.
**jmacdonald** 59:44 So.
**Braydon Kains** 59:45 Thanks. Everyone.
