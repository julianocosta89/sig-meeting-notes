SIG: Prometheus WG
Date: 2026-06-19
Duration: 64 minutes
============================================================

## Zoom Recording Transcript

Arthur Silva Sens 00:05:24 Hello.
krajo Krajcsovits 00:05:28 Hello.
Jonathan Santos 00:05:29 Boom.
Arthur Silva Sens 00:05:34 Seems like we don't have anything on the backlog.
Back over the beach?
krajo Krajcsovits 00:05:43 Or…
Arthur Silva Sens 00:05:45 Sorry?
krajo Krajcsovits 00:05:46 Backlog of the meeting, or backlog in general? I guess you mean the meeting.
Arthur Silva Sens 00:05:49 Yeah, backlog, like, no topics to discuss.
Let me organizes.
And I see Christian here, and I expect that Christian wants to discuss the bridge.
Krisztian Fekete 00:06:07 Oh, yeah, that's correct.
So, not sure what's the process. This is my first time on this call, but happy to.
discuss why we would like to drive this forward, and thank you for pointing me to that open issue about making this part of the spec. I was not aware of this initiative.
Before…
Arthur Silva Sens 00:06:26 Yeah, yeah, no problem. I would just wait, like, 2 more minutes. I expect David Ashbold to join as well, but if he doesn't join, we can start.
Krisztian Fekete 00:06:36 And I also pinged the Auto Rust maintainers, because my shoe… I opened another issue in the, cannot even remember which one, hotel… Rust… Let me try to find it quickly.
Yeah, in the OpenDelementary Rust contribository.
And… Received some.
replies there, and mentioned that they are also welcome to join this co-opmatcher, if they can do that.
It's also a bank holiday in some parts, or at some.
Arthur Silva Sens 00:07:31 Oh, right.
Krisztian Fekete 00:07:33 So, it might, might be tricky.
What are you with?
Arthur Silva Sens 00:07:36 Right, David… David is also based in the US, he probably won't join.
Oh, dammit.
Krisztian Fekete 00:07:45 Yeah.
Arthur Silva Sens 00:07:51 Okay, let's start then.
But, one second.
Sorry for doing this only now.
So, picking up, links.
Okay, so could you provide a little bit of context on this bridge?
Krisztian Fekete 00:08:53 Yeah, absolutely. So, as you all, or most of you probably know that that's an existing implementation for the Go SDK, and… It's, it would be also our preferred way of doing this in Rust-based projects.
Because, just for context, I'm working at Solo, we started out with focusing on application networking, and nowadays we also, cover the AI… the same thing for AI workloads. So we have, Agent Gateway, which is a purpose-built, Rust-based gateway that can be also used for generic purpose workloads, like standard Layer 4, Layer 7 stuff.
But it's also, build with agency workloads and MCP and all the rest in mind.
And we barely decided based on experience that we had.
withdraust.
Istio's new ambient mode. Istio is a service mesh, for the ones who don't know, and Istio has a new mode, a fairly new mode. It's, like, 2 years old, I think, at least, at this point.
And in the ambient mode, you don't have sidecars on your workloads, but you have, layer 7, proxies on demand for certain workloads where you want to enforce Layer 7 policies, but on all of your nodes, the ambient Layer 4 capability is added by a Ztunnel proxy, which is also written in Rust. So, based on this learning, we build Agent Gateway, which is… Quite fast. Proxy?
Arthur Silva Sens 00:10:47 May I interrupt?
Krisztian Fekete 00:10:49 Absolutely.
Arthur Silva Sens 00:10:51 So, you, you started by, saying, you were using Rust for something related about AI?
Krisztian Fekete 00:11:03 Yeah, so traditionally, we've been focusing on standard application networking stuff, because we came from an Istio and, Istio and API Gateway background.
But based on the learnings, with the Rust-based node-level proxy that we added to ECO's ambient mode, we built a new gateway, which is also in Rust.
So these students.
Arthur Silva Sens 00:11:31 This is something that… that your team built, it's not a, like, a CNCF thing.
Krisztian Fekete 00:11:36 These are, like, Istio is part of the CNCF, it's a graduated project.
Arthur Silva Sens 00:11:43 Oh, you also work in Istio? Is that…
Krisztian Fekete 00:11:46 Yeah, yeah, yeah.
Arthur Silva Sens 00:11:46 Oh, okay, cool, cool, I didn't know that.
Krisztian Fekete 00:11:48 And Agent Gateway is not part of daily Linux… it's not part of the CNCF, but it's part of the new Agentic Foundation of Linux Foundation.
But it's not strictly CNCF.
I just wanted to mention it, because these two projects are… both of them are written in Rust, and we have found some gaps, and our users and customers have been reporting Features around… metrics, traces, looks. And for the metrics part.
If you don't want to have a collector in the middle.
then you either use the OpenTelemetry SDK directly, which might not be, preferred in all the cases.
So… hence the topic of… making… Doing, doing the same thing, with, a bridge.
That, we already have in the Go SDK.
Arthur Silva Sens 00:12:50 So, this proxy, you already have metrics instrumented with the Prometheus REST SDK?
Krisztian Fekete 00:12:58 Yes, that's correct.
And we don't want to migrate that to the Rust SDK. For performance reasons, we would prefer to keep using The Rust implementation.
The Ras, the Fisher, Rasp Prometheus, SVK, And we also don't want to force our users to deploy… a collector in the middle, just for the sake of translating that into an ODRP stream.
Some users might only have a OTRP endpoint where they can push metrics to, so obviously managing An intermediate agent or collector is not always preferable, so… I think that… that summarizes the… Core problem, and why we were trying to push this forward.
Arthur Silva Sens 00:14:00 Okay, So, the bridge that we… that David built in Go, this was not part of the spec. This is something that he did on, like, side project.
And, it became quite popular. We're seeing a good adoption on the bridge.
But since it's not part of the spec, like, it's up to the hotel SDK maintainers if they want to adopt or not, right? Like, they have the freedom to say, I don't want this.
But once it's part of the spec, then it's expected that all SDKs and all languages implement this.
I… I've been working with Siho Thomas, I think you… you met him in Slack already, and he's… He's the REST maintainer for the hotel SDK.
Yes. And he is implementing Not the bridge, but he's implementing the… the Prometheus exporter, you know? Like, it's the other way around. Like, from Otales in K, you expose Prometheus.
Krisztian Fekete 00:15:11 I found a little issue, so I'm fairly aware of what's happening there. Cool.
Arthur Silva Sens 00:15:15 Yeah, so I've… I think it would be, like, a big ask.
If we ask him to implement both ways at once.
Because Siho is also doing a lot of other work besides that.
Do you think you can wait as… finish the OTLP to Prometheus.
And then we work on the other one.
the Prometheus 2 OTLP.
Or, like, is this something that you need as soon as possible?
Krisztian Fekete 00:15:50 Yeah, I mean, as soon as possible is always welcome, but we are also kind of busy, but as a side quest, I think you can also start on the implementation on our side, if no one has a problem with that.
So that we can basically push the two tracks in parallel, if that makes sense.
Arthur Silva Sens 00:16:08 So you mean… But then, on our side, which side exactly are you referring to? You mean on the Prometheus SDK, exporting your TLP? Or, like, something on Istio?
Krisztian Fekete 00:16:21 No, so, yeah, there are a couple of things, so… The first thing that we would need is a proper way to read data from the registry, and that is a gap in the AutoL RAS SDK at this point.
I opened the GitHub issue on that, I received no replies at this point, but I think that's fairly straightforward. Like, we could just do what… the auto SDK does. I don't think that that should be too controversial.
So…
Arthur Silva Sens 00:16:52 So you mean you… you create a… you create a fork of the hotel SDK, and then you implement that in a fork?
Is that… is that it?
Krisztian Fekete 00:17:04 this is the… this is the GitHub issue, it's in the Zoom chat, just to make it easier, too, so that we know what we are talking about.
So this is the gap. I think this is the only gap, apart from the actual bridge part, to… to move this forward.
Arthur Silva Sens 00:17:25 Reading.
Oh, you don't… you don't have the protobuf definition like we have in Go.
Krisztian Fekete 00:17:39 Yeah, unfortunately not. But I think it's fairly straightforward, like, we could do the exact same thing in Rust.
Arthur Silva Sens 00:17:47 Hey, wait, we have this repository… let me show my screen.
Discipline, sorry, we have the protot definitions.
And, we have… the goal… Code, which is auto-generated from the protobuf.
I… does Rust have something similar? Like, can… is there a code generator that can generate Rust code from parallel definitions?
If yes, that should be super easy to get… to get merged.
Krisztian Fekete 00:18:34 Yeah, I think that might be… That might be already merged.
But what we would still need Regardless of this, is reading the data out.
of the registry itself, like… Even regardless of this question.
There's no gettherer like… approach that we can, that we can use in the Rust Client SDK to… to do this, I think.
Arthur Silva Sens 00:19:17 Oh… Okay, this… this interface that returns the product definitions.
Krisztian Fekete 00:19:24 Yeah, yeah, yeah. So, we would basically need the same thing in the Rust SDK. But this is why I think this is… this is probably not, controversial, because… It makes perfect sense to have this interface.
Arthur Silva Sens 00:19:38 Yeah, yeah.
So the… Prometheus REST SDK, the maintainers right now, it's you and you alone? Or is it…
Krisztian Fekete 00:19:52 At this point… at this point, I'm alone, which is also not perfect, because, pull request reviews takes some time, so… Yeah.
Optimally, we would need at least another person who can actively focus on the project itself, so that we can Get stuff merged.
Arthur Silva Sens 00:20:11 Yeah.
Cryo, now that you're back, quick context.
To make, like, to make it possible to build a bridge between Prometheus to Autel SDK, The… the Go implementation depends on this gatherer interface, which returns the proto definition.
Of… of the metrics.
Okay, by the way, can you see my screen?
krajo Krajcsovits 00:20:41 Okay.
Arthur Silva Sens 00:20:42 Okay, cool.
We were thinking about… and client model.
From the proto-definition, we auto-generate Rust code, similar to how we do for Go.
And we implement this gatherer.
interface, also in the REST SDK.
One problem is, Christian is the only maintainer, and he doesn't get reviews.
So, the options is either we find another person who is active, and we promote to a maintainer.
or someone who is not Christian implement this, and Christian review?
I think you took a look at the active maintainers for worse in the past. Do you think there are good candidates for maintainers?
krajo Krajcsovits 00:21:48 I, I just know what I heard from, Bronze, Frederick, sorry, that there was one more person.
And he was going to reach out, but I don't know what happened there. I can ping Frederick.
And also, I… I… Asked… inside Grafana, because we do have the Rastanka.
So we have one Rust project.
Let me see if there was some… Reply… I just need to find the statue, because I have, like, a thousand open.
Trust us.
Yeah, I got no reply, Hmm.
Arthur Silva Sens 00:22:54 Christian… Christian, do you have anyone in mind?
Krisztian Fekete 00:23:00 Not particularly from the… from the Rust project itself. Like, I know that there's a couple of works who have been quite active recently, but it's not really… they are not active continuously, just more, like, time to time when they need something.
Do we have other persons at Solo who could be potentially… who are more active on this front, but I don't think one company should probably have already… Or a code owner, or maintainer seats, so if you can have… someone outside of our company that would be, I guess, preferable.
Arthur Silva Sens 00:23:44 Yeah, while I agree that the best is to have diversity on the employers, being realistic, we have several Projects that are only Graphonis as maintainers.
I… it would be… it would be unfair… If… if we block this, because it's all solo.
Krisztian Fekete 00:24:09 Yeah, then I can ask around, and if others are also interested in this, then… and if you are also fine with this, then I think it can be a viable way forward.
Just to speed things up, because apparently it really takes a long time to get anything reviewed, and… Yeah.
Arthur Silva Sens 00:24:31 Could you please start with the client model? Like, generate REST code from the proto? I think this one we can review, we have several people that can.
Krisztian Fekete 00:24:43 I think that's… I think that's already done, so I put another link into the Zoom chat.
Arthur Silva Sens 00:24:50 But…
Krisztian Fekete 00:24:50 Weird.
I'll pick it up.
the latest.
Promitives protobath protons.
Arthur Silva Sens 00:25:04 Why… Yeah.
Now, this is generated code from the proto.
Krisztian Fekete 00:25:11 This is generated… Perfect.
Arthur Silva Sens 00:25:18 I… I… I would love if this… If this is generated from the protobuf.
I think it would be nice to move it here, because if we change the proto, then we automatically update all languages at once.
Krisztian Fekete 00:25:34 Okay, that makes sense. I will… I will take a look at that, create an action item, and… And do that. So you would need this in the client model, repository.
Yep. Okay.
Cool.
krajo Krajcsovits 00:25:54 By the way, have you…
Arthur Silva Sens 00:25:55 Okay.
krajo Krajcsovits 00:25:56 to the wider, like, Rust community, I assume you… You did?
Have you found anyone?
As using it, using primitives.
Client?
Arthur Silva Sens 00:26:12 Could you repeat, Craig?
krajo Krajcsovits 00:26:14 Sorry, so I was wondering if Christian has reached out into the wider Rust community?
To see if others are using the… Romitous client, and if there's somebody willing to step up.
Krisztian Fekete 00:26:28 No, I… I haven't… I haven't yet. I think you mentioned another person, and the person is working at a company who is, behind Linkerdi, another service mesh provider.
And their proxies are also RAS-based, and I believe they use… They use the same.
library for the same purpose as us, so that can… that could be also potential.
away, but I haven't reached out to anyone yet, but I can… I can, take a… a wider look at Scrant.
krajo Krajcsovits 00:27:06 And, sorry, Arturi, if I may have one more question.
Because I missed the… A few minutes here, but, Did you talk about making the bridge part of the spec, or is that…
Arthur Silva Sens 00:27:21 Yeah, like, we've been… like, very slowly, we've been discussing that this was brought up by… by David.
krajo Krajcsovits 00:27:33 I mean, you know, if I have my Prometus hat on, then… It's probably not a good idea, because it's the push model, right? And not the pull model.
Krisztian Fekete 00:27:44 Yeah.
Arthur Silva Sens 00:27:47 Yeah, there's, like, there are… there are very obvious trade-offs. You lose the up metric, you lose all the scrape metrics, There are a few benefits on pushes, though. Like, I think it's easier to batch, it's easier to fine-tune.
I can… like, in Prometheus, if you have a huge page, you… the Prometheus needs to scrape the whole page at once, and if one metric is… has error, you lose the full page, In… in Push, you can… partition that into smaller batches. You can do retries if the backend doesn't… It's not responsive, like… It's a battle of trade-offs, in my opinion.
krajo Krajcsovits 00:28:38 Yeah, I mean, it's not like we didn't have the push gateway all the time. I'm just saying, you know, like, the preferred way is pulled, but, like, I wouldn't block it based on this.
Krisztian Fekete 00:28:48 Yeah, if anyone has the question, I always recommend them the push approach as well, but you know how users and customers can be from time to time.
They might have their unique, limitations or requirements for lots of different reasons, and just having the option, Would be nice.
krajo Krajcsovits 00:29:14 Yeah, I think what comes out of it is that if we make it part of the spec, then it will remain there forever, but you need, like, a sensible default, and I would… Yeah, this is looking in the future, but I would probably make the default the exporter and the pool model, but… Anyway… It's fine. We can continue.
Arthur Silva Sens 00:29:38 Yeah, so if… if we move this forward… Then if we get a specification merged.
then we can request all SAKs to implement this.
I don't think people block. We might have the same problems that we're having now, like lack of reviews.
But nobody would say… would be able to say, no, I don't want this.
Yeah, so… David isn't here today, but the person to talk to is probably David.
Krisztian Fekete 00:30:15 Okay.
Arthur Silva Sens 00:30:16 And you don't need to wait until 2 weeks for the next meeting. I would suggest to reach out on Slack. David Ashbo.
Krisztian Fekete 00:30:23 Yep.
Yeah, yeah, we can also do that. And I think we can also move forward with the other items, like the client model stuff, and also, on the Rust side, we can, make tiny steps.
Arthur Silva Sens 00:30:37 Yeah.
Krisztian Fekete 00:30:37 Awards this goal?
Arthur Silva Sens 00:30:40 And even…
Krisztian Fekete 00:30:40 Not ideal.
Arthur Silva Sens 00:30:42 Oh, sorry, go ahead.
Krisztian Fekete 00:30:43 Even the actual Rust bridge implementation is probably something that can go in parallel with the actual spec, like, because we already have a Go implementation, so it's…
Arthur Silva Sens 00:30:55 Yeah, we have a reference, yeah.
Krisztian Fekete 00:30:57 Yeah.
And I don't really have any crazy exotic, and extreme ideas for the Ross-based bridge. It should be very, very close to the oil and to the gold one, so once we have a spec, it would be very easy to Align both of the reference implementation to spec, or the other way around.
Arthur Silva Sens 00:31:22 Cool. Yeah, let's write down action items. Oops, not this.
This… is that only… only it?
Move the REST code to client model, and implement the gatherer interface.
Each of two.
But, show. You.
And are you okay with, me assigning all 3 items to you, Christian?
Krisztian Fekete 00:32:49 Huh? Yeah, sure.
Arthur Silva Sens 00:33:00 I don't even know how to do this at all inside.
wished.
Krisztian Fekete 00:33:07 I will probably try to start with this third one, because… That would… Speed up, number two at least.
Arthur Silva Sens 00:33:16 Yep.
For the client model, you can ping me for a review.
Krisztian Fekete 00:33:21 Okay, cool.
Arthur Silva Sens 00:33:28 Anything else on this topic?
Krisztian Fekete 00:33:30 No, not really. I think that was all from… from my side.
Arthur Silva Sens 00:33:37 Cool.
And the next one, is this also related to David?
David opened up PR to the spec to preserve JobNet instance when translating Prometheus to OTLP.
We were super, super close to Merge.
But then… our cryo realized that this is gonna be a breaking change for Prometus, so I probably want to be more careful here.
so, what can we do between us?
Without diving here.
krajo Krajcsovits 00:34:19 Well, we were… we wanted to discuss it with David, that's the…
Arthur Silva Sens 00:34:22 Yeah.
krajo Krajcsovits 00:34:24 That's kind of why I, in that… Requesting change.
Arve Knudsen 00:34:33 Maybe we can talk about… Why it should be necessary to… to respect job and instance in OpenTelemetry research attributes. That was my… that's my understanding, although it's kind of ambiguous at the moment.
Arthur Silva Sens 00:34:51 Yeah.
So… Is everyone familiar with the change?
krajo Krajcsovits 00:35:01 I… I was a week ago, but… A lot of.
Arthur Silva Sens 00:35:04 Yeah, me too.
Arve Knudsen 00:35:14 I mean, the… I think… I don't… I mean, it changed a lot since the last time I reviewed it. I think I approved it originally, but then… then at least, I believe, there were… these resource attributes, they were prefixed with the Prometheus dot, at least. I don't remember what else changed.
But at least… I think that part, is more sensible, because as I point out in a comment, that if job and instance are to have special meaning in all the resource attributes connected to Prometheus.
I think that's dubious.
because, I mean, job in Sons, they have, like, a special meaning in the Prometheus context, but I don't think we should, sort of, assume this meaning in… in OpenTelemetry.
Arthur Silva Sens 00:36:09 Dammit.
Arve Knudsen 00:36:17 I think also… I think… I think also… It's problematic that… That, that this, this completely changes, really.
which… which resource attributes are it identifying when ingesting OpenTelemary, when the topic of the PR is… Is… is how to preserve… instance when translating Prometheus to OpenTelemetry, which is the other way around, so it's, like, it's really kind of make… it's really making a very significant change outside of the original topic of the PR. And that actually… that is even conf… that confused even Brian Boram. Like, he… he didn't understand that the DPR changes the OTLP ingestion.
Arthur Silva Sens 00:37:05 Hey.
This pack is aimed at OpenTelemetry SDKs, right? So it's not really aimed at Prometus, but I agree that if metrics from hotel SDK change in a way, it would be nice if Prometius also changed in the same way.
Arve Knudsen 00:37:25 I believe, I mean, I read it closely, and I believe the PR changes the specification for how Prometheus should ingest all telemetry. Should ingest all TLP.
Arthur Silva Sens 00:37:43 It says in this word, with these words, Prometheus, the Prometheus server should change.
Like, Prometus is not obliged to comply with this.
It is super nice, and I think this is a good goal for Prometus, but we are not obliged to.
Like, this spec is aimed for hotel SDKs.
Arve Knudsen 00:38:09 I… I mean, there is a part of the spec which says how to convert OTLP metric points to Prometheus, and that is what Prometheus follows.
Arthur Silva Sens 00:38:19 Yeah, yeah.
Arve Knudsen 00:38:20 I mean, we…
Arthur Silva Sens 00:38:21 Not a black.
Arve Knudsen 00:38:21 It seems… it seems strange to me that this spec should be written with… with the idea that Prometheus should not follow it. That seems strange to me, but… But I think in any case, I think my point stands, in any case, that the topic of the PR is to… to change, is to… is to preserve job and instance when translating Prometheus to your TLP, but it actually changes also the opposite direction.
Arthur Silva Sens 00:38:57 It changes both directions when, like.
when translating OTLP to Prometheus, we are changing this as well.
krajo Krajcsovits 00:39:08 Yeah, you can look at the diff… I tried to do two examples, so, in my comment.
On this PR.
So if you look at the diff, we can work it out backwards.
So… the, which direction is this? So, this is the… I assumed.
Arthur Silva Sens 00:39:33 I think…
krajo Krajcsovits 00:39:35 Yep.
Arthur Silva Sens 00:39:37 I think it's easier just, let's see.
Prometheus to OTLP.
Arve Knudsen 00:39:44 Yes, and that's, like, that's the direction that the topic is supposed to be about.
Arthur Silva Sens 00:39:50 And then you're saying that we also have changes below here.
Arve Knudsen 00:39:55 Correct.
krajo Krajcsovits 00:39:58 Yep.
Arve Knudsen 00:39:59 And those changes, those changes are very significant.
And I think those changes are dubious.
Because they, they, they change, you know, significantly.
how openly OTLP is to be converted to Prometheus.
And I, and they, and they… That changes independently of… of the stated goal of the PR.
Arthur Silva Sens 00:40:34 Yeah.
Arve Knudsen 00:40:34 So I think… I think that change, it has to be discussed in… in separation.
As I said, I think… I think that the change basically implies that that we project the Prometheus meaning of a job on instance onto OpenTelemetry. I think that's, I think that's a very questionable one.
Arthur Silva Sens 00:41:03 10 feet, Prometheus.
That's supposed to be… Well, that's not included.
I think… Okay, and I am noticing that it's also removing this… Bart?
Which… Prometheus build the translation based on this phrase alone, mostly?
says the service name, service namespace, and service instance ID is a unique Triplet.
I think… If this is true, it would make everybody's life easier.
But, this… this uniqueness for the triplet is not really working out in reality. Like, we are seeing this problem in, for example, the MySQL receiver, Postgres receiver.
And, Jack Berg tried to put this in his pack, and it got refused.
I think this… losing this is the, like, the biggest breaking change, right?
Arve Knudsen 00:42:26 I don't… from what I remember of reading this, I don't think that's exactly the case, because I think what the spec says after the PR.
is that, first of all, you should respect job and instance research attributes. If they are present, they should be identifying.
if they are not present, you fall back on the… on the current triplet, which is service.namespace, service.name, and service.incidence.id.
I'm fairly certain that that's what the spec says after this PR.
Arthur Silva Sens 00:42:58 Okay, okay.
Arve Knudsen 00:42:59 Source of one, it, it… the, the, the PR proposals to, to, to… treat JobNin instance as special, open telemetry resource attributes, which are identifying, and… and, and, and, also Are, are, are sourced from… corresponding Prometheus labels, which I think is a very dubious assumption which one should not make.
So I think that's a problem in itself.
to make that assumption. And second, it's going to be… It's going to be backwards incompatible.
I, I… I foresee… I don't know if it's going to happen, but I foresee that there will be users of OpenTelemetry who have job and instance… job and or instance resource attributes from OpenTelemetry, which will then be treated by Prometheus.
As if they, are identifying.
And, and Dave, and Dave will not like this.
And rightly so, they should not like this, because it doesn't make sense, in my opinion. They shouldn't be treated as something special.
Arthur Silva Sens 00:44:18 Yeah, Cryo?
krajo Krajcsovits 00:44:19 Yeah, more specifically to what Arva was saying, I was reading my notes now. So, if the… If that user has Joban instance right now, It's not respected, it's overwritten.
Yeah. With service name, service names, etc. But with this change, it's respected, so suddenly you break an assumption that somebody could have made.
It's, It's, like, a nuance, but there's always somebody that does this, and then gets annoyed, you know.
It's a question how you want to deal with this. I realize this is development status, so… you might say that you document it and, I don't know, shout very loudly that this is changing, but…
Arthur Silva Sens 00:45:08 Yeah. I was gonna say… I think Prometheus… And I'm part of this, like, I'm also part of the Prometheus team. But I… I think Prometheus made a big mistake.
when it… It tied… it told… It documented that the OTLP endpoint is stable, while this pack that we tried to follow is not stable.
So now we… we are putting this back in, like, the hostage situation. We cannot make… it's unstable, but we cannot make changes because it breaks Prometheus.
Arve Knudsen 00:45:45 But my argument is that it doesn't… it doesn't bring.
Arthur Silva Sens 00:45:48 It doesn't solve a problem.
Arve Knudsen 00:45:50 it doesn't break Prometheus, it breaks open telemetry users, and rightly so, because it makes an assumption, which I think is… Very dubious.
As I said, it makes the assumption that job and instances carry special meaning in OpenTelemetry, and they don't.
Arthur Silva Sens 00:46:08 I think the problem that David is trying to solve here is the problem that Prometheus already solved with the keep identifying… I forgot the name of the configuration, but, like, the people are getting confused that their service name is getting translated to job, or the other way around, where the job is being translated to serviced, like, attributes. Like, they don't… they… they just want things to stay as they are, no translation.
Like, oh, Prometheus did this already, and this configuration option that Prometheus did does not exist in the hotel site, and David wants the same thing.
They, they, they want… Labels should not get renamed to something else.
And I think this is a fair, fair problem to solve. I think this… this is confusing, indeed. We just need to understand how to make this change in, like, in a way that works with Prometheus.
But it… yeah, it's gonna be a breaking change. I don't… I don't see a way of doing this without breaking people.
Arve Knudsen 00:47:13 I… I don't think it's been sufficiently explained or defined why it is necessary to make this change.
So, like… the topic of the PR is to… is to make sure… is to ensure that job audiences are preserved when translating from Prometheus to OTLP. Sure.
But then we have to… I think we have to define the use cases that should be, that should be, solved.
And then it should define How they need to be solved.
There's no, there's no, like, explanation why Why job and instances have to be respected as open entry resource attributes?
like… So, so I think what I'm saying, and probably Carlos are saying, is that it… it's… it's very questionable on the face of it, that job and instance should be respected as alternative resource attributes, like, special attributes.
And there is no justific… there's no concrete justification as to why.
Arthur Silva Sens 00:48:20 So, would you like to see Dave… David doing what exactly? Like, update the PR description with the problem he wants to solve, or, like, just give up on the… on the change at all?
Arve Knudsen 00:48:37 I think it needs… I think the problem that the PR is supposed to solve needs to be properly defined, like… It's sort of my… Am I wrong in thinking that the problem is that… job and instance labels from Prometheus are not… Properly preserved than a round trip.
Arthur Silva Sens 00:48:58 Yes.
Arve Knudsen 00:48:59 That's my designing originally.
Arthur Silva Sens 00:49:00 My understanding as well is that service… service instance, service name, and also the other way around, job and instance, they are getting renamed, and people are getting confused with this one.
Arve Knudsen 00:49:13 Yeah. So then we have, like, the basic problem that we are trying to solve.
But I think we need to define concrete use cases that we want to solve, and then we need to kind of define how to solve those use cases. I think that those definitions are missing, and there's just… there's just an assumption that what is prop… the breaking change in the PR will resolve the use cases in mind. That's just an assumption, it's not… it's not defined properly, in my opinion. Not… I cannot see it, see the definition of it.
I am.
Arthur Silva Sens 00:49:54 Right?
krajo Krajcsovits 00:49:55 Oh, yeah. By the way, I came to this issue from the issue, not the PR, and the issue had a question about whether to introduce a breaking change, and there was no discussion. And I thought that this was… I didn't even realize there was a PR, so I posted a… A comment on that.
Issue, saying that… We can break things if we make things better.
But, like, I don't know how long… Yeah, one of those.
I'm not sure which one.
No, the other one, I think.
Yeah.
So… So my point was to only make a breaking change if it makes things better.
And, the question is, You know, is it worth baking things for the existing users.
To make it easier for future users to use it.
Like, is that the trade-off we are making here?
Arthur Silva Sens 00:51:05 It seems like it, yeah.
krajo Krajcsovits 00:51:08 So is it… But then it's maybe worth… You know, making… Like, I hate configuration options in general, because they introduce just more problems.
But maybe one way to do it… No, no, I don't want to make it optional.
I don't want to break it up, so… Yeah, I think I agree with Arv that the use cases and better motivation is in order, and And I'm not sure… It makes sense to… boot.
Both directions in the same pull request, because if I see JobN instance, that doesn't necessarily mean it's coming from Prometus, basically. But if I see service.
name and service names Eastern-sided, then I… I think I know it's coming from OTRP. So that's… that's the assumption that Prometus made.
Arthur Silva Sens 00:52:13 Can you… do you help me write down this feedback? I think we need to… like, we can give it in Slack to David, and Oh, we… I think you were saying two problems, right? One.
Arve Knudsen 00:52:27 I, I can write, I can write my, points there. Alright, thank you.
I agree, for example, with what Grayo said, that we shouldn't have both directions in this PR.
Arthur Silva Sens 00:52:39 Cool.
Arve Knudsen 00:52:40 It's… it's sort of like… it's sort of like, confounding two diff… to the… two different problems.
At least.
Arthur Silva Sens 00:52:49 Hey, it's easier.
Arve Knudsen 00:52:50 it confuses people who see the PR, and they think it's only about the OTLP to… sorry, the Prometus OTLP direction, and then when I explain that it goes the other way, they, they, They, they are young, they are surprised.
So I think that's a big, a very big symptom that this PR needs to, it's doing too much.
Arthur Silva Sens 00:53:16 Yep.
That's fair feedback, let's… let's give.
Arve Knudsen 00:53:19 I'm gonna… I'm gonna ride my place.
Arthur Silva Sens 00:53:24 Are you writing on this, meeting notes, or already in Slack?
Arve Knudsen 00:53:31 I'm going to add my points to the meeting, that's what I assumed.
Arthur Silva Sens 00:53:35 Cool. Yeah, sounds good.
Yeah, okay.
If… if the… he updates the PR to be only one direction.
Are you still not… you still need… want to see changes, right?
It's not only about being two directions.
Arve Knudsen 00:54:04 I will have to re… Did, I would have to read the piece and, you know, and kind of consider those changes for what they are.
Arthur Silva Sens 00:54:16 Cool.
Arve Knudsen 00:54:16 I cannot say anything before there, and it's actually revised.
Arthur Silva Sens 00:54:21 Boop. Alright.
Arve Knudsen 00:54:48 Yeah, so I… I mean, I'm just going to finish my points async. We don't… I don't think we should wait on… wait… wait on me to finish.
Arthur Silva Sens 00:54:56 Alright.
So, one thing that… I am also a little bit worried, So this resource attributes, translation, and, target info, and the upcoming entities.
I have a feeling that To stabilize them, we will make breaking changes.
I cannot tell exactly what, but, like, I have a feeling that this is being discussed for so long that, like, there's definitely something incorrect there.
Arve Knudsen 00:55:28 Sorry, I'm not talking about the… that the entity model will carry… Carry information about what our identifying resource attributes?
Arthur Silva Sens 00:55:38 Yeah, yeah.
Arve Knudsen 00:55:39 You're referring to?
Arthur Silva Sens 00:55:41 But .
Arve Knudsen 00:55:42 Also, there's interesting.
I've studied this, and I don't see how compatibility… I would need… if you think it's going to break backwards compatibility, I think you would need how to point out how, because I… I don't see that myself.
Arthur Silva Sens 00:56:04 I… one example that I see, for example, is, like, the problem that you've been battling with the Postgres receiver.
Hi, Postgres, is not considered a service by the maintainers or the hotel technical committee, and they will… should not have the service inside ID and the other service-related attributes. So, when translating an OTLP message that does not have the service resource attributes, how do we translate Dis, Uniqueness into the target info metric, into the job and instance labels.
Arve Knudsen 00:56:47 So the… the problem is that those… those OTLP payloads, they don't have a service.instance.id, for example.
Arthur Silva Sens 00:56:56 Yeah.
Arve Knudsen 00:56:57 Okay, but… but you're… what we were talking about was how entities would break backwards compatibility. How would entities be a problem in this case? That's what I don't understand.
Arthur Silva Sens 00:57:10 I… I… I'm not really saying that it's gonna be a problem for sure, like, but I… I have a feeling… That this will require a lot of changes in the spec?
And .
Arve Knudsen 00:57:22 I'm fine.
Arthur Silva Sens 00:57:23 Yeah, breaking change.
Arve Knudsen 00:57:24 I'm… because… I actually see that the end… will, will, fix the, oh, the hotel exporter problem… sorry, the, the Postgres, exporter problem.
because the entity model will let them define which are identifying resource attributes. So, that's why I'm curious how you see that the entity model would cause back, you know, breaking changes, because I see the opposite.
Arthur Silva Sens 00:57:55 Okay, so let's… let's say that Postgres… resource attributes are like, I don't know, table name and database name. This is hypothetic, I'm just saying random, random things.
We… with the entities, we're able to tell that those two are identifying, and we… when converting to Prometus, we… we build a hash, or something like this, and it becomes a service inside IT.
From this, can we translate back to exactly table name and database name?
I'm thinking…
Arve Knudsen 00:58:31 too late.
Arthur Silva Sens 00:58:31 translation.
Arve Knudsen 00:58:33 I… I guess, y-y-yes?
if… I mean, via target info, if you don't translate, you will… you will get the… the original label names.
And… and there's… so… So what is it you have in mind that would not work? That's what I don't really see.
Arthur Silva Sens 00:58:57 Yeah, I'm not really sure if it's not gonna work, I'm just not… I'm not really understanding how it's gonna work.
the round trip. Like, we translate something to Prometus, and then from what we have translated, we can migrate back to the same identifying attributes.
Arve Knudsen 00:59:15 But I think round trip is a different problem. That's, like, a problem of itself.
But we were talking about whether entities would make things, and they would cause any breaking changes. According to, you know, my argument, they will actually make things easier, because Because they will solve the problem of the Postgres exporter that it can instead define its own resource IDs. Sorry, its own identifying resource IDs. Yeah. So I only see the entity model being, A solution in that use case.
When it comes to David's proposal.
I actually think that we should not try to change the… the default identifying research attributes that Prometheus operates with, we should instead wait on the NTD model, because when the NTD model arrives.
Prometheus will, respect whatever the identifying resource attributes are.
As they are encoded by the entities.
Arthur Silva Sens 01:00:24 I'll let Cryo go first, because he has a raised hand, and I'll answer this one.
You're muted, Cryo.
krajo Krajcsovits 01:00:36 Crap.
All right. So, yeah, I wanted to say that we opened a huge topic in… over the last 5 minutes of this meeting, so I think we should not do that. I think maybe next… maybe let's put on the agenda for next time to think about the round trip with entities.
like, at least identify What we want to achieve, and what areas it would even impact.
And I also wanted to call out that I have a PR open on the spec that is awaiting merge, so I don't know who to… Bug about it. I'll put it into the, chat.
Arthur Silva Sens 01:01:17 Which PR?
krajo Krajcsovits 01:01:20 I put it into the chat. Maybe I can put it.
Yeah, I put it into the chat.
Arthur Silva Sens 01:01:44 So the problem that I see here with waiting entities is that entities is very slowly moving, like, they don't get the… they don't have the… They don't have enough hands to make progress quickly.
And, there's so many things depending on the stable spec.
For example, collect… to stabilize the OpenTelemetry collector.
they… we need to stabilize Prometheus Receiver.
We cannot stabilize the Prometes receiver while the translation between LTLP and Prometus is not stable.
And then, if we wait for entities, then… We cannot stabilize the collector, because entities are not… It's not ironed out.
I'm not saying that we should just do whatever, just to declare things stable, but, like, it would be awesome if we could find solutions without entities.
A cryo?
krajo Krajcsovits 01:02:51 Fair enough. I would put that on the next meeting's agenda, then.
If you don't come up with something offline, but… you know, regarding something like the Postgres… Exporter, or… yeah, exporter.
Like, Prometus will not be able to, like, guess what are the identified attributes, so either we agree on something, and we already have an agreement included, or It… you… you cop out, and you make it configurable, and say that this sucks, but entities will solve it later.
Arthur Silva Sens 01:03:24 Yeah.
krajo Krajcsovits 01:03:24 So, yeah, I don't know. I have to go soon, but I'd love to continue the discussion.
Arthur Silva Sens 01:03:33 Yeah. Arv, could you give the feedback to David in Slack? We've tried to discuss in Slack more.
And then next meeting… Yes.
We continue.
Arve Knudsen 01:03:45 We can do that. I'll finish typing our points into the doc, and then I can paste them into Slack for our discussion with David.
Arthur Silva Sens 01:03:53 I… I will be on PTO the whole… the whole July.
So, next meeting, I think I'm already out, but I hope you… you can do… make progress with David without me.
Arve Knudsen 01:04:07 Yep.
That's the evil datasets.
Arthur Silva Sens 01:04:11 Yep.
Cool.
Alright, thanks everybody.
See you next time.
Arve Knudsen 01:04:17 Yup, whatever.
krajo Krajcsovits 01:04:18 Love it.
