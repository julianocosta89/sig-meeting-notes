SIG: Arrow SIG
Date: 2026-10-20
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

Pierre Mariani 00:03:01 Hello, folks.
Drew Relmas 00:03:16 Hello, everyone. Good afternoon.
LAURENT 00:03:53 Hi, everyone!
Pierre Mariani 00:03:57 Boom.
Joshua MacDonald (Microsoft) 00:04:05 Hello.
LAURENT 00:04:08 I don't respond.
Nev Wylie (MSNev) 00:04:11 Ayy.
Joshua MacDonald (Microsoft) 00:04:37 All right, everybody, put your name in the list, and I think we can get started, except I was worrying that nobody has triaged new issues, so we could do that.
Right.
Link is still broken.
Okay, 5 new discussion, needs discussion.
Needs deciding… Oh my god, so many.
Are we ready?
Let's see. I think we should go through the needs discussion. There's too many deciding to go through all at once.
Some of them are new, some of them are not.
And I know I created one new issue, but we don't need to discuss it. So, if you feel the same, we can start here.
And… While we're going ahead, we can also note that there is an agenda item, so maybe… Run through discussion quickly.
So, last week, we had actually seen this one.
4366.
And I think we've now done most of the work that was under discussion.
Drew, is that true?
Drew Relmas 00:06:21 Yes, I was actually just typing up a notice about this to post in Hotel Arrow Dev in the Slack, and then I was gonna comment it here. For those of you in the call, we've made the change, so that contrib-only PRs We'll only need one authorized approver.
Anything outside of Contrib, or things that touch both Contrib and other core crates.
We'll continue to need to, as it has the past few weeks. But this should improve the velocity of folks working on their own, relevant contribute interests.
Joshua MacDonald (Microsoft) 00:07:02 Great, great.
Can we close it?
Utkarsh 00:07:06 Okay, optimal.
Drew Relmas 00:07:08 Yeah, I believe… Ukarsh, you're gonna speak up. It's not exactly what Utkarsh was proposing in the issue, but I'll leave it up to him if it's close enough.
Utkarsh 00:07:17 Yeah, I think the main issue is resolved for sure, like, which is basically have more velocity in the contrib-related PRs.
But now I think, like, the only thing where it differs from the issue, the actual solution, is in the issue, I suggested that if… Not any approver or any maintainer's approval.
Is… should be enough.
If it's… if it happens to be the case that the owner of the component is also one of the approver or maintainer, then it's good enough.
Otherwise, we can apply the same policy that we apply with core nodes. But yeah, I think that implementing all of that may not be worth it. It's just a… It's just one more layer of, like.
Strictness that we would add.
But, I mean, I'm happy with the current state as well, because the core issue is resolved.
Joshua MacDonald (Microsoft) 00:08:13 Gotcha.
I would be okay with closing this. We can open it again.
I will leave it to somebody else. So… let's see… I think back… Next, I know that Noah's not with us today, He did file this issue, which I've read once.
And Mark needs discussion.
Mainly because I feel myself uncertain about the life controller and the, rollback and rollout mechanism, so I don't feel confident.
But this basically asks us to clarify some of the things that were identified during a PR, The PR is not… Has not merged, and is… oh, it did merge, okay.
So, we might be able to close the issue, but I don't think we should stare at it now and.
LAURENT 00:09:09 do that. No, I think we can't, because it has been merged, but I mentioned a few issues, and I think it's, Let me see… I don't remember if it's… can you reopen the DSPR, just to…
Joshua MacDonald (Microsoft) 00:09:25 Right.
LAURENT 00:09:26 the historian.
Yo.
Joshua MacDonald (Microsoft) 00:09:33 So, yeah, you may…
LAURENT 00:09:34 for the…
Joshua MacDonald (Microsoft) 00:09:35 Comment, this comment…
LAURENT 00:09:37 Yeah, I think we had some discussion with Noah, and we end up with some, conclusion, saying that we have some issues here and there, and it was like a follow-up.
Joshua MacDonald (Microsoft) 00:09:49 Okay.
LAURENT 00:09:49 I remember when. That's right.
Joshua MacDonald (Microsoft) 00:09:51 No, let's do this.
LAURENT 00:09:54 So I think we… can you maybe, assign it to me?
the…
Joshua MacDonald (Microsoft) 00:10:01 Yes.
I can.
LAURENT 00:10:05 Thank you.
Joshua MacDonald (Microsoft) 00:10:07 Cool. Okay.
So then, moving forward, or backwards, forwards, I noticed that this issue of mine is very aligned with the topic of the agenda item.
And I'm going to propose that we move that sort of, like, affiliated discussion I also know that Pierre was interested in working on that, and he's here, so, We'll talk about that in a bit.
Let's see, so then Jake filed one about, vendor semantic conventions.
Jake?
Jake Dern 00:10:46 Yes, I can speak to this one a little bit. So, for folks that don't know, last week we ran into a situation with the traffic generator receiver where Basically, the semantic conventions Registry upstream, which is what the traffic generator uses by default, added support for some new unref attributes, and our version of the Weber toolchain did not support that, and so what ended up happening is we broke a bunch of unit tests, and also all of our benchmarks, which kind of depend on the semantic conventions Registry. And I think this exposed, like, a few problems around You know, one, like, kind of non-determinism in the benchmarks and the possibility of those being influenced by things upstream. But then also the fact that, you know, our unit tests and our benchmarks, as well, like, kind of require access to the internet in order to function.
And so while I did kind of fix the former issue by just pinning a default internally, and then also making sure that various benchmarks and things were pinning to a specific remote version of the semantic registry.
Obviously there's still, like, some… some risk there, in terms of reliability, just one for having to go over the internet, and also, you know.
requiring that GitHub is functioning well, and you can always clone that registry.
In order to run stuff, so… I was thinking it might be a decent idea to, for the purposes of our unit tests, and our benchmarks, to not have to always be pulling down this, the semantic conventions registry, and just vendor a copy of it. And we can automate updating it.
If we… if we want to, I think that's probably a good idea. But that'll just basically eliminate that… that instability. We won't have to worry about it anymore.
Joshua MacDonald (Microsoft) 00:12:34 Great. I know that I had seen that being part of our slow build problem, and I wanted to fix it as well. The, like, cloning of an extra repo.
Like, I don't know, something seemed funny about it.
Couldn't we just… Yeah.
Jake Dern 00:12:52 And just, you know, for transparency, I did go take a look at the full upstream, like, registry. It's about 2.3 megabytes. If we don't feel good about that, we can cut it down, or maybe swap to something else, I think, for the purpose of you know, certain benchmarks and unit tests, it doesn't really matter too much, but I think it's a reasonable enough size.
Joshua MacDonald (Microsoft) 00:13:13 Got it. Yeah, I was thinking… I guess I was thinking that we could get away with less than that amount of data on every test, but it's not too much.
Good, thanks for measuring it.
LAURENT 00:13:23 I think a future, I'm totally supportive also of that. I was… I'm thinking that, What will be nice, once we've finalized the entire story about the… semantic convention integration, client SDK, pipe safe, API, blah blah blah.
That we are… on which we are operating now for multiple months.
Inside this project.
Once we have this semantic convention for our own internal Telemetry, then we can use this… we can use this semantic convention.
It will be anyway, version into this project, and we can use it to generate traffic. That is, in fact, a good representation of what this same project is… already generating, except that we can use the traffic generator to do it.
Joshua MacDonald (Microsoft) 00:14:20 Cool idea.
Jake Dern 00:14:21 Yeah, I think that's a great idea. I will also just point out, in case we're thinking maybe we would like to defer this work for that, I think even if we were using our own internal semantic registry, most of the work here is going to be updating things to be referencing a local registry rather than a remote one.
And then also fiddling with things like benchmarks, to make sure that semantic conventions Registry is mounted to the containers and that kind of stuff.
So we can, we can still work through all of that and vendor the, you know, the, the upstream registry for now, and then just simply swap over later, would probably be my, my proposal.
Joshua MacDonald (Microsoft) 00:15:05 Sounds good.
All right, so, now we edited that, the ordering changed. We're gonna go next to, this Docs RS build failing.
maybe important.
Good to know.
So, I don't know what this means, but we should fix it.
LAURENT 00:15:41 Yeah, I don't know yet. I know that Albert mentioned that, but I didn't, Look at it, to be honest, so, yeah, it was yesterday.
That's something we need to fix, yeah.
Joshua MacDonald (Microsoft) 00:15:59 Okay, and… Lately, when we go through the stale issues, we've been having, like, Too many.
problem. We could do that quickly.
Gearing up for a discussion about JSON, We hope.
Oh, this is not so bad.
I feel like every day I hear about request crypto dependencies, we probably have to keep that open.
We… we are working on memory limits, so I don't think we need to discuss that again. I'm gonna mark those not stale.
I remember this issue, return data into two, there… this may be resolved already by some of the recent refactoring.
This was…
LAURENT 00:16:45 Yo!
I think,
Joshua MacDonald (Microsoft) 00:16:49 Let's open it. So, the way I remember this, like, if you're a retry processor, you only need to have the return data for NAC, and it's currently a single bit, so you get the data back for NAC, even when there's no use for it.
LAURENT 00:17:06 I think we need to double check.
Joshua MacDonald (Microsoft) 00:17:09 So, I'll take a look at that.
at least it seems like a potential. Proposal. Structured retry hints from exporters, including retry after… okay.
I remember this one. We do not have… I think still, at this time, any way to return structured information, like, A retry after, potentially.
LAURENT 00:17:36 Yeah.
Joshua MacDonald (Microsoft) 00:17:36 this sounds to me like return context, something I've, you know, you could imagine. But also.
Something you might distinguish AC and knack for, just like the last issue.
So I think we can probably keep this one open.
LAURENT 00:17:54 I think it's something on which we should work soon, because, I mean.
Because we have this generic literal processor, yeah, we should allure This, retry after, thing.
Looks like an important aspect to… Yeah, so… to support.
Joshua MacDonald (Microsoft) 00:18:21 Go ahead.
Drew Relmas 00:18:21 I was gonna say, I have one question here, which is… Do we have an official stance or position on if exporters should Actually be doing their own retries or not.
Off the top of my head, Azure Monitor Exporter does have a few internal retries, but we often pair it internally with Quiver, you know, which has its own persistence guarantees.
But for the generic exporter, Should we maybe discourage having.
LAURENT 00:18:55 Yes.
Drew Relmas 00:18:55 Internal contrace.
LAURENT 00:18:57 I think that's the entire logic of this project being, more composable and, and providing, Component, like the retry processor, infuser, The fan out, the batch processing, and so on.
They are there to just avoid Exporter authors to re-implement the wheel every time.
Drew Relmas 00:19:24 Gotcha.
LAURENT 00:19:25 Yes.
Drew Relmas 00:19:25 Okay, so maybe there's a follow-up here, you know, at least for the Azure Monitor Exporter, maybe we can use that as an example. I could foresee an issue to remove its internal retries and delegate that work in our generated config to a retry processor. Okay.
Joshua MacDonald (Microsoft) 00:19:42 So you can imagine how this is going to require some of the work that we've done on codecs, because the reason not to do that is that we've already spent some CPU to format the correct outgoing protocol, and until you have a way to return that encoded data.
to the retry processor, like, it's just doing extra work to re-encode that data, and that's.
LAURENT 00:20:04 Yeah.
Joshua MacDonald (Microsoft) 00:20:04 want to do this.
LAURENT 00:20:06 That's a very good…
Drew Relmas 00:20:07 Okay, that makes total sense.
LAURENT 00:20:09 Yeah, and I think it's, something, to be honest, that I didn't include into the… All the CADEC argumentation.
don't take into account this aspect of the story, which is, I think, a very good aspect, too. Yeah.
Joshua MacDonald (Microsoft) 00:20:27 Yeah, and that's why the… in the Go Collector, there's an exporter helper that includes a bunch of stuff that all has to kind of know the protocol, and this is an opportunity for us to, like, decompose in a better way, because we can vary the codec. I think that's cool as well.
LAURENT 00:20:44 Yep.
Joshua MacDonald (Microsoft) 00:20:46 So then, last.
Utkarsh 00:20:47 Yeah, I think about this one, I just had one comment. I think the original issue that LAURAN had created about the P data correct thing into… copy the link and paste it to the chat. So I, I haven't looked into it yet, but I think, yeah, the Quiver durable buffer processor or the query engine can support that. Right now, it only has, OTAP and the other, I guess OTLP, plain OTLP byte support, but if we extend the… Quiver processor to work well with PData codec, then we could get rid of issues like this, where the exporter has already encoded and compressed the data in a certain format, and we could make quiver Persist the final data.
that shows.
LAURENT 00:21:39 Yes.
Utkarsh 00:21:39 of the network, and… Yep.
Just wondered.
LAURENT 00:21:44 That's… that's, that's really cool, because if we… Yeah, I mean, more than 100 person have that, because that will extend the… the perimeter, significantly the perimeter of this project. So right now, we… we can support now two major modes. One is… We… we have whatever format in… for the input.
And, we are working in a Let's say, password mode.
So we don't need to decode, we can, and that works well if… Between the receiver and the exporter, everything that is in between.
Is… is… does not require to… to look at the way that the data is encoded.
So if we can just rely on the name of the codec, the type of the value.
Maybe some estimates regarding the size.
We don't need to decode.
It is that this, Hotel Arrow server Can be used to root information that are not necessarily even elementary related, and it looks like inside Microsoft, it's, definitively also something of interest.
And we are using, that, we could use that, for example, to… to, batch and root information between two Kafka topics.
Now, if we have this quiver thing that is now pluggable, codec-aware.
And does not require to understand what is inside the… the Pilata message.
Then we have another very interesting capability for this possible mod, which is persistence.
In a, in a local queue.
If you combine that with Kubernetes and the stateful deployment.
I think it's, it's, it's super cool.
Joshua MacDonald (Microsoft) 00:23:51 Very good.
I agree.
I also filed an issue this week, about the Quiver storing context for the multi-tenancy issues as well, so we're looking for a lot out of Quiver, Aaron.
Aaron Marten 00:24:10 I had left some comments, by the way, on your PR, Josh.
Joshua MacDonald (Microsoft) 00:24:15 Very good.
Thank you. And that is a PR of mine, the RFC0006, which is, still open, and I have it on my desk.
Okay.
Did… how did I get back to this sales list? Okay.
These are… The ones that are still deciding, sorry. Okay.
There was one more stale.
in our list, and I think we want to move on to this JSON discussion. This… Future consistency model is now 6 months old.
Do we still need it?
LAURENT 00:24:59 material consistency model.
Can you, move up? Excuse me?
Yeah, yeah, assign it to me, because right now, I'm… I think this is…
Joshua MacDonald (Microsoft) 00:25:21 and partially fixed, even by the one that I mentioned this morning, 3865.
What's that?
Or did I get it right? It was… no, I didn't get it right. It's one of the ones that CJO just merged, or I merged for CJO. But I will assign this to you. Thank you.
LAURENT 00:25:39 Yeah, and I will, double check.
Joshua MacDonald (Microsoft) 00:25:43 Because I know that that change was to reject rollback-based… Reconfiguration errors, and that might have been related.
Okay.
I think it's time that we move away from those old issues onto the new… to the agenda.
So… Let's see, this actually is the one I was thinking of.
We got a… indenting problem here. I will fix that in a second.
Not in front of you. So, LAURANT, you're up. We want to talk about the pluggable codec first, and then we'll bleed over into the Microsoft JSON receiver and talk with Pierre about how I think we should have some common code.
LAURENT 00:26:35 Can you open the PR file?
Or if you prefer, I can also share my screen, it's up to you.
Joshua MacDonald (Microsoft) 00:26:41 Why don't I stop sharing, thank you, and I'll…
LAURENT 00:26:45 Okay.
Joshua MacDonald (Microsoft) 00:26:45 tests.
LAURENT 00:26:47 Okay, okay, sounds good.
Okay, can you see my screen?
Joshua MacDonald (Microsoft) 00:26:58 Yes.
LAURENT 00:26:59 Right.
So… I don't know if everyone followed this adventure regarding the pluggable CADEC system, so very quick.
Summary of what it is.
until a few weeks ago, the system was, so the PDATA message, basically the unit that we A receiver is producing, processor is consuming, producing, and An exporter is consuming this PLATA message.
was an enum, with two major variants. One was OTAP, which was the preferred representation for eData messages.
Another one was a special case.
For a TLP.
where, if we have an OTLP receiver.
And we are in a very basic configuration. We do some routing, we do some batching.
and we… and we just have an OTLP receiver, OTLP exporter, so a relatively simple, pipeline. Then we were able to run in a pass-through mode, which was, a nice optimization.
no desalization at all, even, of TLP messages.
And we observed multiple times, with the CAFCA receiver, with the syslog receiver, and I think also, the file log receiver is also another motivation behind that.
The fact that, it would be super cool if we can enabled the engine to support different codecs.
And to create some kind of, C'ad, to… whatever codec you have, let's say CSLOG batch codec.
If we are in a pass-through mode, so it means that… let's say that we have an… we don't have it, but let's say we have it, we have a syslog exporter, we could be in a situation where we duplicate the syslog traffic to two syslog destinations. In that case, we don't need to decode.
a syslog at all. So, being able to support this concept of codec so, Pilata message become… something with two variants, again, but one is the OTAP, the native representation, the only one where we are able to do Data processing.
general data processing. And another one, which is, the codec, the plaggable codec, variant.
And we rely on the specific codec implementation to Determine on the fly when we need to decode Whatever format, represents the codec to a tap.
Or a tap to this codec if we are in the exporter side.
Plus a few additional, basic operations.
Like, merge and split to implement, a butcher?
And, And also the ability to determine the type of the… the batch information that is encapsulated into this connect.
And the number of items.
With that, we can, in fact, implement generically the batch processor, the type router, the… I'm sure that I forgot, so a few, a few others.
But, and we can also implement, in a generic way, some internal instrumentation.
When this internal instrumentation is enabled, we can, for example, follow the number of Items, process, input, output, bioprocessor, these kind of things.
So, we already merged 4PR, It was a long adventure, and this Pierre is about, PR5, it's about, enabling syslog.
And, I think that's the first example where we have now It's… PLATA is no longer only OTLP and OTAP, but could be also CSLOG.
So I introduced this, the name of this, codec is named syslogbatch.
But because… this Pilata message will represent not a single syslog message, but a batch of syslog message. So it will be the responsibility of the syslog receiver To aggregate as much as, syslog message.
Based on the configuration of the existing system receiver. There is no change on this side.
So the… Now, the… we are moving from… for the syslog receiver, from the responsibility of listening to UDP or TCP, Determining the framing of the system message.
messages.
and decode them, and generate an attack representation of that. So we are moving from that to… obviously listening to the TCP UDP, Determining the framing of those messages, but just… adding… or creating a PDATA with the C slug batch codec.
with… the… just the binary representation of a series of text messages that we just read on the UDP or TCP socket.
And, and the constructor of this, PLATA message also can take optionally The number of, entries, and because the syslog receiver is obviously, Detecting the boundary of every message, so we know this number, so there is no need to To recompute it, And then, because right now, we don't have a C-slug exporter, I will say that Even if the decoding is not done directly in the receiver, it will be done along the way, somewhere, in the first processor that will require to look at the data, or at the minimum, to the exporter that will be part of this pipeline.
So we… we move the decoding from the receiver to a different place. That's what the… it's done there. And… I use also this opportunity to… To make, an interesting optimization.
So the… for these two, C-slug representation.
We have, again, on the CPU usage of 37% to 32%, and I will explain why, we end up with that.
Obviously, that's something that could be done with the previous receiver.
But, I included this, optimization in the… In the codec.
And also, a small optimization in terms of, minimal usage.
So now, how this optimization has been done.
And I think because Utkarsh is with us, You will… let's see where it is… oh, I think it's there?
Yeah. So… In this scene, we, we were, so, some, especially in the, in this, IFC, The… the ear is not… is not necessarily there.
In the format of the date. So, in order to parse it with this, thing.
We basically added the current year, and then we end up with a regular date, and then we parse it.
The optimization is basic. It's just… Avoiding this logic, and just parsing directly the date, and considering that we know the year as a parameter of this parsing method.
And that's how we end up with this optimization.
Otherwise, I think there is no… major other things.
But that's, for me, the first example of a codec that is no longer purely based on open telemetry representation.
Joshua MacDonald (Microsoft) 00:36:17 Cool.
I look forward to reviewing this when it's out of draft. Any comments?
Utkarsh 00:36:25 Yeah, so, LAURAN, this PI… yeah, the benchmarks here, yeah.
So you said this 37.98% reduction and 32.43, that's the date-time-related benchmark? Or, like… Yeah. Okay.
LAURENT 00:36:41 Yeah.
Drew Relmas 00:36:42 Is there a way we could maybe consider separating that out into its own PR to isolate the change?
I know we've…
LAURENT 00:36:53 Yeah, I'm already at the PR5, and soon PR6. I can do that, but it's always, Additional work, to be honest, but Yeah, if, I mean, feel free to put that in the review, and I will take it into account.
I found that motivating to have this improvement with the CSLOP patch codec, just to demonstrate that, This approach does not prevent us to be efficient or performant.
Utkarsh 00:37:34 Yeah, so I'm trying to understand, like, the other existing benchmarks that… we already have some existing benchmarks for Syslog. Now, that probably… would have to be updated to use the codec instead of, the…
LAURENT 00:37:48 Bossler.
Utkarsh 00:37:49 library that we used to have, no? Okay.
LAURENT 00:37:52 No, because the, it's, I mean, the receiver has been updated.
Utkarsh 00:37:59 Okay.
LAURENT 00:38:00 And the receiver is now… I mean, it's fully connected. The receiver is using the codec attach.
And there is no change at all in the configuration.
So, all the benchmarks that we have, for example, in the continuous benchmark or the nightly benchmark, they will be automatically updated.
Utkarsh 00:38:21 Yeah, but then the benchmarks now would… I mean, if there's no decoding happening, then the benchmark numbers are gonna go down… Significantly.
LAURENT 00:38:29 existing benchmarks.
Utkarsh 00:38:30 Oxford.
LAURENT 00:38:31 No, because, it's currently impossible to avoid the decoding.
Because, basically, you don't have… There is no way to construct a pipeline where you can leverage the passport.
fork, for syslog.
So, all the…
Utkarsh 00:38:53 Okay.
LAURENT 00:38:56 So I don't think we will observe, I mean, we will observe this game, no?
But I don't think we will observe, A reduction that is so dramatic that, I need to check one aspect. If we have a new exporter.
And we don't have anything in between.
I will double check that.
But I think that's the only possibility where the, The decoding will… the lazy decoding will not be enabled.
Utkarsh 00:39:31 Okay.
Yeah.
LAURENT 00:39:33 But, yeah, I will, I will double-check with them.
Utkarsh 00:39:35 I'm holding this.
Pierre Mariani 00:39:37 Laura, I'm trying to wrap my head around what's happening, so… So there is one aspect, which is this PR is part of a larger piece of work, which brings in the decoder becoming lazy.
which will eventually enable a pass-through, and therefore, you know, no decoding, no encoding. So that's the value there, I think. And then orthogonally to that, there's this, Date parsing trick, which is bringing the 40% improvement there, right?
LAURENT 00:40:09 Go.
Pierre Mariani 00:40:10 Okay, so… Okay, yeah, I guess I'll read more about the overall goal of the lazy decoder, I think that's the key here.
LAURENT 00:40:21 Yeah, yeah, well, I will, I will, so back to what I asked Drew, I will, split this Pierre in two.
Yeah, I think, I will ask an agent to do it. I don't think that will be too much work if you are more comfortable with that.
Joshua MacDonald (Microsoft) 00:40:42 That sounds good.
Excuse me.
LAURENT 00:40:45 Okay, so… I think that the… The next, is not really yet a PR, but that's the next step.
And I think that will, inform a little bit more on the perspective, I mean, things that we can imagine to do with this codec approach that we were… we were not able to do before.
don't take into consideration that. I renamed it in PR5, and it's not yet merging to this PR6, or future Pierre Pier 6.
But the… If we look at Africa, for example, we recently someone, I don't remember, work on that, but someone inside Microsoft work on the text format integration into Kafka.
And, if I understood well, it was basically, we received some JSON format.
which are not OTLPGs, then?
And, we… map… the… each individual JSON document into… A single… a batch of a single entry, a single log.
log record.
And then we emit that from the Kafka receiver, And that would be, processed by KQL or PL to extract the name element into, into this JSON representation, and map that into… in fact, QQL for now is only able to sit on that. OPL is not yet able to do it. But we extract the element from this JSON, document.
And we… generate, for example, an event, which follows the… the open TMLP format, so it's… It's nice.
With the Codex system, what we can do is… So, collect are, first, they are a generic construct that they can be used and reused in different contexts, in different receivers.
You are no longer creating a codec for just a type of receiver, you are creating a codec for the engine, and then… Receivers and exporters can use them.
So we could imagine that we have, a G-Zone codec, a witch, Let a receiver accumulate different documents.
And once the receiver decides that we accumulated enough, creating… the receiver can create a pilot a message with this codec.
For this amount of, It is on the document, so it's no longer… One PDATA message per… per GISN document, but potentially multiple, so we get there for free, an improvement.
And, and then… If we need to decode the data.
The codec will be used to determine the mapping.
So that's… that's an option. We could imagine a JSON, a generic JSON codec that, is coming with a configuration where you specify the mapping.
Or, we could say, It's… Purely text, we don't know what it is, so there is a text codec, we don't try to decode it, but we encapsulate multiple lines of text.
And we let a more generic solution, like KQL or OPL to decode this text and construct, A representation of the corresponding, Set of, open telemetical, signals.
So these two models could be implemented. So, once we… we have that in mind, it means that codec or Not only things that are discoverable when the binary is constructed.
we, it's… they are working like extensions, so there is a mechanism to register codec implementation, and during the build process, and more specifically, the The linker will discover the different… CADEC implementation, and we'll expose into the binary the list of available codecs.
And by default, their name and their implementation is well known. And for example, when the syslog receiver is, initialized, it is asking to the engine, can you give me the codec name slog-batch batch?
If this codec exists, and because it's a default codec.
It will return the CADEC instance, and we'll be able… we'll be able to use it directly.
Now, if we have… Binary that are extending the… the default version of the Hotel Arrow project.
Adding new codec, they will be automatically discovered.
And they will be available So we could imagine, in Contrib, for example, this text codec, And, And then, or let's say the JSON codec.
And the JSON Connect maybe needs some configuration, depending on which pipeline you You integrate it.
It would be nice to specify the rules to map the… this generic JSON document into an open telemetry-compatible, batch of signals.
So… the idea here is… By default, you get those predefined codecs, but you can, if you want, you can, create your own. It's not well represented here, but I changed slightly the… it's not yet merged.
But, I introduced, basically, a new codex section, Where you can provide a name to a collect that exists, you specify the implementation, and then you specify the configuration. And this configuration is up to the collect implementation.
I mean, the interpretation of this config section for the codec is up to the… the codec implementation.
So, if we want to implement, like I said, a JSON codec doing this mapping, that will be a feasible. An example of that is the… The… forget this representation, I changed it, but imagine that here it's OTLP bytes.
So the OTLP bytes codec, which already exists, but not yet configurable.
You will be, it will support, by default.
the validation, which is based effort. It's basically what we have currently in the project. But we discussed in the past multiple times the fact that it would be nice if someone wants to be Very strict on how to decode this, Otlp bytes.
And, and want to refuse anything that is not compatible with the… with the spec.
This parameter could be used, and then we have, a different branch to decode the OTIP bytes. I think you, Pierre, you were working on this stuff, if I remember well.
the CU codec infrastructure for TLP bytes.
We'll enable… will authorize us to… Yeah, to provide the two modes with the default mode, which is the current one, but someone could use the strict, for a specific pipeline, or for all the pipeline.
Joshua MacDonald (Microsoft) 00:49:08 This would allow you to protect against, like, unrecognized fields in the protobuf.
LAURENT 00:49:14 Yes.
Yeah. Yeah. So, I'm… I'm just enabling the option, I didn't implement in the strict mode.
And I'm using that as an example of why it's interesting to have collect configuration.
The other one is the GZON stuff, where, yeah, if you have mapping rules and you want to export them directly into the codec, that could be an option.
And I'm sure that we could, imagine in the future, depending on the format, some… Yeah, configuration, that will make sense.
Pierre Mariani 00:49:51 a long, quick question so I don't lose track. So the… The basic requirement of a codec would be that we would know how to merge messages, we would know how to concat messages, we would know how to count items.
LAURENT 00:50:06 No. Okay. It's more flexible than that.
Pierre Mariani 00:50:10 Okay. Yeah, go, go ahead.
LAURENT 00:50:13 Yeah, you have basically a series of capabilities.
Decode on code.
Merge split.
Kund.
And, a codec, does not need to implement everything.
So you could have only… You could have a codec that only know how to decode a format to a tap.
And that's it. It does not know how to count, it does not know how to merge fields, so in that case, the engine will automatically decode that into a tap, and then, because we are in a tap and we decode it on the fly.
Then we get the standard capabilities, merging, splitting, hunting, and so on.
And if you don't, for example, for the CSLUG batch codec, there is no encode, implementation that could be added later on. But, right now, it's only able to decode from a text representation to… to a text.
Pierre Mariani 00:51:19 And if… if decode is not possible.
Then we just envelope the… the arbitrary binary of the codec and pass it through.
in an export message? In an OTAP message, or…
LAURENT 00:51:36 I mean, the dec… the… The encode is only useful if you have an exporter.
That require this format.
So, in the example I used with this C-Slug, we don't have a C-slug exporter.
So I, I… the… I mean, nothing prevents the codec router to implement the uncode part of the C-slug batch codec.
But you don't have, because there is no exporter currently that will require it.
If we integrate a syslog exporter, then, If the same codec is used and there is no extension to support the encode, the, During the configuration phase that will be detected, and the pipeline will… will not be, compatible with the engine. And the engine will say, okay, this pipeline can be deployed.
Pierre Mariani 00:52:46 Thank you.
Joshua MacDonald (Microsoft) 00:52:48 I would like to step in and interrupt us a bit, because we've got 10 minutes left, and this has been very relevant, but I want to make sure we get a chance to hear from some of the others here. I know Nev from a long time here, Nev has joined us to talk about, their work on a JSON receiver, so it really does connect with the previous topic.
It sounds like this, and I had found an issue, more or less, saying that, hey, it bothers me to see so many JSON implementations already, but, this is taking it a step further. Like, we've got multiple, like, different JSON formats that we would like to receive.
both through, plain HTTP or through Kafka. And Nev, would you like to speak? I think that what we're looking for is, you know, to discuss using codecs for this.
Nev Wylie (MSNev) 00:53:39 Yeah, so… I think long-term?
I think, you know, doing the decoding for this would work really nicely.
The main reason for me joining this is I've got this receiver fully functional, and I have had it functional for months, and I'm now just upstreaming this here.
It does a little bit more than what LAURENT is talking about, though.
on receipt of the HTTP request, because this is primarily for browser.
It does have to… it's not gonna be lazy, it's got to pull it apart.
It has a bunch of config, which I think I put in the PR.
So that you can map it based on the framework.
And then effectively what it's doing as part of its own config is effectively applying whatever the current OTLP semantic conventions are. So it might get a field from standard Azure Monitor Input, or 1DS input, and put it into one or more attributes, because it just creates a no-tap log record.
Or it can actually validate it and throw it away, and say, hey, nope, I'm gonna reject that event, you know, that single line, or I'm gonna reject the entire batch.
it probably differs a little bit from the codec, and I'm uncertain whether it would be a single codec or two, and that this supports two different formats. One is a single JSON blob, which effectively is an array of JSON blobs, which… where the blob is the event, or it's line separated. So… you know, you could say there are two codecs, you could say there are one codec that happens to say, hey, if the first character is a bracket, I'm gonna deal with that, so…
LAURENT 00:55:28 Is there a name, Nev to this, JSON format.
Nev Wylie (MSNev) 00:55:34 Yeah, so it's the standard Azure… so there's two different formats that are being supported in this, and they're being supported purely by config.
So the… the JSON… the line separated, is JSONX, I think it was, and the other one is just straight JSON. Like, you know, if it's an array of JSON objects, it's just JSON.
Where's my… I can give you the exact name, but apart from that, the actual format of the objects are Microsoft proprietary formats. So, the actual events that are encoded as JSON blobs are either the Azure Monitor.
JSON blob, or it's the internal Microsoft Common Schema, or 1DS is the SDK that we have it on, JSON blob.
LAURENT 00:56:23 So, personally, what I would recommend is to… Yeah, to create two codecs.
Looks like the format is specific to Microsoft, if I understood well.
Nev Wylie (MSNev) 00:56:35 The individual fields, yeah, so… so effectively, the… There is some top-level fields, like name, time.
And then we say data properties. So, effectively, the outer envelope is specific to Microsoft, and then it just has config to say, hey, I know how to… effectively map JSON fields based on, like, XPath-type definition to pull it apart. It does get a bit deeper because of the browser, and that sort of says, if the event name field of the entry is this, then I'm going to apply this set of rules. If it's, like, this one, I'm going to apply this set of rules.
So that we can… Validate the individual events slightly differently.
But yeah, they add our own codec decoding.
Yeah, I'm…
LAURENT 00:57:28 So, what I'd like to say, following what you just explained, I think, so first, converting your code into the Connect implementation is just moving your decoding put into the… a track that represents the codec, so… It's, it's, it's relatively straightforward.
But doing it, that will give you the option to imagine that inside Microsoft, you have some PubSub system, or Kafka system, and for whatever reason.
you would like to have those GSONX or GSON messages, That's Arrow.
received, stored in Kafka, and you don't want to re-implement the same logic in the Kafka receiver, so the idea of Bosco deck is really to to share the decoding and encoding across receivers, across exporters. So, different transport.
But if fundamentally the data by itself is the same.
okay, you have different transports, Kafka on one side, PubSub on one side, HTTP receiver is another example of transport.
A gRPC could be another one, but at the end, it's still the same format.
So that's why the CADEC approach is, I think is very nice in that case.
Nev Wylie (MSNev) 00:58:49 Yeah, I agree that, you know, effectively, you know, pulling this out and abstracting it in to be a generic codec, which is fully configurable.
you know, I think it's a long-term goal.
I just have a really tight set of timeframes that I'm not sure I'll… doing that at this point. Like, I'm happy to say, hey, assign me an issue to refactor this to… to be codex.
It's a bit like, I think Joshua also, pointed out, I've got the separate exporter, which is doing the reverse. It's taking OTAP and sending out to JSON, which I think is his discussion point that he's got here.
Again, I think that's all relevant too.
I'm just a little bit concerned about time.
Joshua MacDonald (Microsoft) 00:59:35 Yeah, so can I just step in and say, I think we should not… not block UN Nev, and also, like, all the… all this discussion is so that we can, you know, inform the codec design that LAURENT is working on. So, it's useful that we discussed it. Thank you for the presentation on that. Does sound like two different… you know, actual codecs. What I'm seeing here is, like, you know, many protocols can be described as either JSON lines or JSON blobs. And, it sounds like a good test for LAURENT's configuration.
story that he just told earlier would be to, like, see if we can actually turn your level of sophistication around this JSON codec into reality over, you know, months ahead, not to block you now.
I also… I mean, it sort of seems like we're talking about migrating towards, like, these sort of shared receivers and exporters that are basically, like, transport-specific. So we would have an HTTP receiver, a gRPC receiver.
a datagram receiver, and the datagram receiver does, you know, syslog, but it also does StatsD. One day, we'll have a StatsD receiver, and we'll do that with the same receiver as what we do syslog with, I think, and that sounds like JSON receiver can do both the… what Nev has asked us, as well as you know, OTLP JSON, as well as OTLP protobuf over HTTP, I like this direction, it sounds pretty good to me.
LAURENT 01:01:05 Yeah.
Nev Wylie (MSNev) 01:01:07 Yeah, I…
LAURENT 01:01:07 Personally, I'm not against the… so, sorry, I'm not against to… to, to have this, this Pierre merge, But I'm against… in the future, once we have the PR6 merge, to have… That's repeated.
Because we should avoid, at any cost, to have situation where we do… we have some ad hoc approach, where now we put the effort to have a more generic approach.
Because otherwise, we will have a constellation of different ways of doing things, which is not great, in my opinion.
So, okay to merge that now, because we are, like, at the boundary of this exercise, but personally, I will, I will, I will not accept any PR in the future, which are not following this path.
Nev Wylie (MSNev) 01:02:00 Yep, if I can just share my screen for a second, I can give you a little bit of a view of all the different components I'm playing with, if I can remember, had I share my screen on here? There we go, share… And it's going to be… This one, so this should look pretty familiar to you.
To you, LAURENT, because I think you wrote this. But this is the admin portal.
So, this is the working instance that I've got in my test infrastructure.
LAURENT 01:02:31 Nice.
Nev Wylie (MSNev) 01:02:32 So, what I'm thinking, like, what we're working on at the moment is, I've got, effectively this export on. Can you see my mouse at all, or… or not?
LAURENT 01:02:42 Yeah, yeah, we can.
Nev Wylie (MSNev) 01:02:43 Yep, yeah, so I've got, effectively, the exporter, which is in Phase 3.
I've got this one here, which is the, you know, Phase 1 that we're just talking about.
I also have an extension that adds JSON support to this, so both of these are actually receiving… well, in fact, this one actually receives protobuf or JSON, but I just extended the existing one.
I've got this one here, so this is actually running as an Azure Container app.
Which has a bit of a problem, which is why this thing exists, that I'm highlighting.
And that it only allows one inbound HTTP connection.
But of course, both of these receive HTTP. So, what I've done is I've hacked this thing, which goes… this is actually a no-op forwarder, so that the framework doesn't throw it away, but it has wired up into it. It's, in proc calling into these.
And it's actually also got a reverse proxy, which is how we're seeing the, This admin portal live, because it's actually… everything's coming through this receiver.
What I would propose is, I don't think this is a viable option, especially with the codec, that we say, when I get to the point of being able to do this one.
that's when I effectively convert this Into a codec. So, effectively, this would just be… become a… because this supports options, like, it's all for browser, so it supports a HTTP inbound request, it supports the browser options request, and it can say, hey, when the URL is X, I'm gonna use codec Y.
And then… then it would just come down into, like, this request here, which really… this is… This one's a little bit like the attribute. It does a little bit of extra things for HTTP request.
And this is also a bit like the attribute processor, which does some redaction of some of the fields, so… which, again, I think both of these can be merged into the attribute processor. I just didn't do it at this point.
LAURENT 01:04:43 Or the transform processor, which is,
Nev Wylie (MSNev) 01:04:46 Yep.
LAURENT 01:04:46 a version plus this,
Nev Wylie (MSNev) 01:04:49 Which we can have at a bigger discussion later. And this one actually uses MaxBind's GOIP, so it affects.
Reads the, the inbound… client IP that was populated here into the Cool, and effectively… decodes and says, hey, this is the longitude and latitude, right? So… These are all the individual bits and pieces that I'm coming, but I'm thinking, right now, at least for the timeframe I'm on, I need to get this one… Oop.
It'll bother too far.
I need to get the exporter and the… this one here in… in a fairly short time frame. I am targeting it as alpha.
So… and I can put into the README, hey, this is going to change, so effectively all its config will become a… you know, shift out to the, the codec, which I think we can do, but it does a little bit more than the codec, but it's got to work with the codec because of the validation thing, but… Anyway.
LAURENT 01:05:53 It's a great demo, I think it's demonstrating the… Definitely the power of what we are building, and we already know that we will progressively simplify what you just explained. Yeah. Not only with the codec, but if you are using the transform processor, some element of what you have here in this pipeline will be merged together. Correct, yeah. That's excellent.
Nev Wylie (MSNev) 01:06:20 Because we just say, hey, we have an OTLP protobufed codec, a JSON OTLP JSON codec, and the Microsoft JSON codec, and it's just the one receiver just gets it all, so…
LAURENT 01:06:31 Yep.
Excellent.
Joshua MacDonald (Microsoft) 01:06:36 All right, thanks everybody. We are over time, so I think we have to call it.
I'm sure we're gonna hear more about JSON in the future, and this does look like a really good use of codecs, so thank you, Nev, thank you, LAURAN, thank you, everybody.
LAURENT 01:06:50 Yep, thank you. Have a good week, good week. Awesome.
Joshua MacDonald (Microsoft) 01:06:52 So, if you're still here, look at Jake's comment in the chat, that's also relevant. I'd like to think… talk about that more. Thank you.
Nev Wylie (MSNev) 01:06:59 Yeah, cheers.
LAURENT 01:07:01 Okay, thank you.
