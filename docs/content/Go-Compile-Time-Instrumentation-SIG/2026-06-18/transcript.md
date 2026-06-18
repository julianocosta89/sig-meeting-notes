SIG: Go Compile Time Instrumentation SIG
Date: 2026-06-18
Duration: 36 minutes
============================================================

## Zoom Recording Transcript

**Kemal Akkoyun** 05:08 Good morning, everyone.
**Azhar Momin** 05:14 Good morning.
**Kemal Akkoyun** 05:24 If you have any agenda items, feel free to add here.
Let's give everyone several minutes. People said they will attend.
Okay.
Good morning. So, Dario is here.
**Huxing Zhang** 08:21 Okay, good morning.
**Dario Castañé** 08:24 Good morning.
**Kemal Akkoyun** 08:25 This year, so maybe we can just start.
Okay… So… I think we have an agenda item from… Ushin about, observability that I talk?
**Huxing Zhang** 08:50 Yeah, I actually have a document, I will paste it.
**Kemal Akkoyun** 09:01 Yeah, sorry, I haven't had a chance to review.
The proposal here?
**Huxing Zhang** 09:05 We can be…
**Kemal Akkoyun** 09:06 Bye.
**Huxing Zhang** 09:06 Yeah, we can discuss this meeting, because it's close to the deadline.
**Kemal Akkoyun** 09:11 Yeah, sounds good.
I was planning to review it today, but yeah, let's discuss it. If you can share the link, and maybe… I can share this, open it, and talk about this.
Okay.
**Huxing Zhang** 09:49 Yeah, I can have a brief discussion, a brief introduction, there's two, two titles, two proposals. One is the, like, Comparing different, kind of approach of different languages. How do we do auto-instrumentations?
And… No, too, to… like, coming from the idea that I think, Jorasi has mentioned, the, the… how we initiated this, it's because, we have, like, Java, we have auto-instrumentation, and, Python, we have auto-instrumentation, but for Golan, we… Didn't have, such kind of, instrumentation, so we… have a… hey, this is, equiv… equivalent instrumentation for… for Goland, and, And this is, I think there's something… equivalent for both different languages. We can compare in both, approaches from different languages, and, By introducing this to let more people know about this, this project.
And I think there's another chance, it's the… Because the… the EBPF instrumentation for Golan is going to sunset, I think, and we have a chance, maybe, to… To promote our project, by this way. This is the first idea. The second idea is to combine the… go… the goal… Compile time instrumentation with the… the OBI, the Open Telemetry eBPF Instrumentation.
And… which is, very… also very… project with a lot of active commit… commits to that. And there's one… one talk we have has been accepted in Kubekong, China.
this year is about this, just OBI and the OBI project. So we… I think the OBI project is very active, so we can, by connecting with this project, maybe we can have a better chance to 22P Accept.
Yeah, this is what I'm thinking, so I'd like to hear your comments or thoughts.
**Kemal Akkoyun** 12:30 Okay, so first, like, to keep the record straight, yes, the OpenTelemetry eBPF Goal project is sunsetting, but they are merging it to the OBI, so the functionality is still in there.
So… I don't think we are, like.
we have an opportunity there, right? So OBI will be the next thing, because it's already in there. I will be giving a talk, OBI versus compile time approach, in GopherCon UK this year, so… I would be happy to help with that as well.
But what I liked, actually, is the first proposal.
Right? But, like, probably we need to change the abstract a little bit, and maybe the title, but, like, talking about auto-instrumentation strategies in general in OpenTelemetry.
I think it's, like, it has a broader audience.
And we can, like, focus on that, right? This is how you auto-instrument with Java and Python and Node.js and Go in OpenTelemetry, talk about the strategies, like, downsides, what would be the result. I think we have a better chance of getting accepted.
Because when we just focus on Go, it is not enough, and I think so, it's so niche. And we can talk about OBI with this strategy as well, because OBI also does a lot of stuff.
And we can talk about the compile time instrumentation, and yes, it won't be the first, like, it won't… beyond the spotlight are sick.
But that would be more beneficial for the community, and… By this way, we can also talk about our project.
Yeah, that's… I'm leaning against Proposal 1.
but maybe changing the, like, the… I'm okay to mention the languages in the abstract?
Plus, I will also comment on the document, but I don't think we should mention them in the title. We can come up with a more catchy title on, like.
OpenTelemmetry Auto Instrumentation, how it works.
For example, something like that.
**Huxing Zhang** 14:51 Yeah, I think, if you have can… have any comments, we can, like.
I think you can directly… you have permission to edit that, or, yeah, we can polish it directly, and we can make it finalize it.
And the submission will be in, like, I think will be in one or two days, the deadline will be, so… Okay. I'm thinking that we can… maybe we can support… submit both of that, but, that will be fine with me. Yeah.
**Kemal Akkoyun** 15:26 Okay, I have… I will… I will edit this, and I will also share my… auto points, like, the talk on OBI versus compile time, which got accepted for GopherCon. I can also share that, and maybe we can change the wording a little bit, and… Which is basically your second abstract.
Yeah, and maybe we can resubmit that as well.
**Huxing Zhang** 15:52 Yeah, I think, Hai Bin is, is joined, has joined, and Haibin has, connection in the OBI. He's participating in that mistake as well, and contributing to that, and he has.
**Kemal Akkoyun** 16:06 Posting.
**Huxing Zhang** 16:08 one of the, I think it's a maintainer, or, I don't know where he's done, and he can… he can reach out to them and, see if he can invite someone from this, the OPI side.
And to… as a co-speaker, I think.
**Kemal Akkoyun** 16:28 That would be amazing, because that would increase our chances of acceptance, right?
So two SIG… SIGs come together and talk about this, it would be better. Yeah.
Do you want to do that, Habin, or, like, I can also try to… Porched the idea in their channel.
**Huxing Zhang** 16:50 Yeah, I think having already have some connections, I think he will do that.
**Haibin Zhang** 16:57 Yeah.
**Kemal Akkoyun** 16:57 Sounds good.
**Haibin Zhang** 16:58 However, to… I will to… to the… OBI material about this topic.
**Kemal Akkoyun** 17:05 Okay, I will then, yeah, let's talk about some action items, I guess.
So, having… I don't have the ads, so… Reaches out… OBI, I think… To find a core speaker.
And I will edit, the… Proposal?
Ship this… I'm not done with it.
And I will also share the… my, like, accepted talk for OBI versus… Compile time.
So, we can then focus on that.
Cool, anything else?
**Huxing Zhang** 18:33 Yeah, I think, We can find… maybe we can… we have to… finalize this proposal very soon. I suggest to, in one or two days, we can also reach out to Rasid for… Additional command, comments?
I'm looking for the deadline of this event.
**Kemal Akkoyun** 19:02 21st, I think. It's… it was 21st of June.
So, it's Sunday.
**Huxing Zhang** 19:09 Yeah, so we have… we don't have too much time, because… so we… we need to make it… I think we can make… we should make it, fast.
**Kemal Akkoyun** 19:21 Yeah, it filled with, like, I will… Today or tomorrow, I will conclude everything on my side.
**Huxing Zhang** 19:29 Yeah, for the speakers, I think if you're interested in the first one, I can also be a co-speaker from… from my side, we can… I can talk about the other approaches, because I have some knowledges about Java, Python.
Or set first, yeah. And for the second proposal, I suggest, hyping and, some folks from OBI side.
Together. What do you think about that?
**Kemal Akkoyun** 20:04 Yeah, fine by me. I think, like.
These could be placeholders as well, right? So, They allow all the changed speakers, so if we have enough representative from the SIG, that would be fine.
**Huxing Zhang** 20:20 Yeah.
**Kemal Akkoyun** 20:22 So yeah, but for the first one, I can… you can write my name as a co-speaker, but I'm not sure if I'm gonna make it. And if we can't find anyone from the OBI, or the second one, I would be happy to talk about it as well.
Because I will be talking about it on August anyway, so…
**Huxing Zhang** 20:42 Yeah.
Okay.
**Kemal Akkoyun** 20:50 Cool. Any other topic?
About this? Any other comments?
Okay.
I think the next topic is all… on me?
I updated this R umbrella issue and milestone.
And I think, like, you have already checked, Yehan already checked.
I think we have a consensus, but, like, we have issues that are not claimed, right? There are some, like, like, issues that… I think these should be in… thing, but, like, yes, we need to assign people. So, if you already have If you already want to work on any of these, like, maybe let's try to assign these, to people.
Azar on this, I think.
Yes, it should be.
Sign him.
He's actively working on this as part of, also, the LFX program.
Yeah. Do you have… have you checked any of these issues? Like, who… if anyone wants to claim any issue from here?
We have, for example, for Kafka, I think we already have a PR, we just need to… like, merge it. Log… I think Logris also, this is also a PR.
If I am not mistaken, and OpenAI also has a PR. So, yeah, these are… No? I remember a low gross PR. Did we close it?
Abin, do you remember?
**Haibin Zhang** 22:53 I, I remember.
**Kemal Akkoyun** 22:56 You or D.
**Haibin Zhang** 22:56 Yeah, yeah, I will do this.
tonight.
**Kemal Akkoyun** 23:03 Okay. Yeah, that's, like, we are in the… like, this is the last step, and most of the work is clearly… nearly done.
So I would say that, like, please check these out, and feel… for the maintainers that you can directly assign Any of these issues to yourself, and because we also have some, like, small fixes, this should be, like, super easy to make sure they are done.
The official worksite documentation is kind of a big one.
I think Yiyan, like, did some work on that. I think he's busy, but, like, maybe he wants to finish that?
Yeah.
**Dario Castañé** 23:48 Kamal.
We have a volunteer. Viaga is asking for one of these issues.
I understood, like…
**Kemal Akkoyun** 23:59 Okay, was it on the… yeah, chat, sorry, I wasn't following the chat.
Yeah, feel free to, like, check the issues, like, this is the issue number, and it's in the document as well, here. I mean, you can… comment on any of these issues if there is no PR, or if it's not claimed.
And then… Yeah Exactly. Comment on the sub-issue, comment on the V1 issue, and then we will assign that to you, and you can work on it.
Thanks for the help, that's really appreciated.
And some of these, they have PRs, we just need to review, make sure that, like, what is the missing part, whatnot. So, yeah. Last steps, everyone. So, I think if we just, like, focus on this, this is… One week off work.
That's it. Should be fast.
**Azhar Momin** 25:00 I actually had a proposal, regarding moving the instrumentation package to top level. I already commented on the issue, can you please take a look at that?
**Kemal Akkoyun** 25:12 Okay.
We turn… Always migrate move?
What was the… do you remember the issue?
**Azhar Momin** 25:26 It's instrument, yeah, this one, top level.
**Kemal Akkoyun** 25:32 I'll plug it.
**Azhar Momin** 25:33 dude.
**Kemal Akkoyun** 25:38 Oh yeah, Lauren.
My pro is the following structure. Yeah, I'm… That's exactly… Sounds good to me.
Mimicking the goal contribute report and similar approach.
Should work.
And then share hook APIs… Yes, it all contains, yeah.
I like the idea, yeah.
So… Oh, I can say that, like, Yeah, I've been con… Nope.
Officially.
And then, like… We can move on from there.
**Azhar Momin** 26:51 I'd be happy to work on it, if there's no…
**Kemal Akkoyun** 26:55 Yup.
I mean, let's go step by step. I think you already have something that you are working on.
So…
**Azhar Momin** 27:08 Yeah, I have a PR open for it. I'm waiting for reviews, it's a huge PR.
**Kemal Akkoyun** 27:14 Okay.
**Azhar Momin** 27:14 It takes some time to reopen.
**Kemal Akkoyun** 27:17 Yes.
Okay, Dan.
You can check it out. Yes, we need a VRs, we have some PRs to… Merge.
Yeah, this is, for example, one of the works we just need to double-check the latest issue.
Some of them are blocked because Sharia wanted to have a look. Yeah, we have the logist one.
Yeah, like, some of the open issues we already have PRs for. I think we just need to make sure these are merged.
This is closed.
They're the colors.
Yeah, we need to review this one for the Kafka instrumentation, for example.
So anyways, so that means, like, we need to, as maintainers, we need to do some reviews, merge them, like, we need to do some, like, small issues, but let's focus on wrapping this up for, like, in the next week.
we… so that we can met our goal, right? We said we would like to finish everything By June, and yeah, June 30th, and… We are close.
Russein, do you think, like… Yiyan will have time, or Habin will have time next week, only working on these?
**Huxing Zhang** 28:54 I think, we can definitely… working on that. Yiyang is, I think Yiyang is on… on vacation, but he's online, and having… Okay. Having you can, Check out that.
**Haibin Zhang** 29:12 Okay, no proper.
**Kemal Akkoyun** 29:14 Thank you so much. I mean…
**Huxing Zhang** 29:16 target from this, deadline, June… June 13th, I think. Yeah, it's a good, very good, important milestone for us.
**Kemal Akkoyun** 29:26 Yes.
Yeah, feel free to ping me, or, like, ping Dario on, like, the reviews. We will be responsive for the next week, so… yeah, let's… let's keep the momentum going, and merge everything, and call it V1. Then we can also work on maybe a blog post with Jurassi to announce that we did the V1, whatnot.
Let's… then we can start making some noise.
Oh, I think Ian is also here, okay.
Cool. Any questions?
Any concerns about the roadmap?
Cool Okay, June 30th, like, whenever we finish that, we have 12 days. We can do this!
**Huxing Zhang** 30:27 Yeah, let's do it.
**Kemal Akkoyun** 30:31 Cool. Alright, this was all the agenda items, I think, for today. Has anyone anything else to discuss?
Going once.
going twice.
All right.
Thanks, everyone, for attending.
We can keep it short this week, and go back to work, and shipping the V1.
**Huxing Zhang** 31:05 Okay, bye-bye.
**Kemal Akkoyun** 31:07 Bye-bye.
**Azhar Momin** 31:09 From my bike.
