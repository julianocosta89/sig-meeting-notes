SIG: Swift SIG
Date: 2025-06-19
Duration: 24 minutes
Zoom Recording URL: https://zoom.us/rec/share/DG7Oj44drPB1dyn6jQmbuHnNuDA_a4dr8Gv-ukmLK1SkaZTzHuIIebTToFXpw4Kw.QV_-VKYM1ZhvsOXM
============================================================

## Zoom Recording Transcript

**nacho** 00:18 No one second right now.
I will not.
**Vinod Vydier** 00:34 Hey? Natural? How are you?
**nacho** 00:37 Fine.
Yeah, I was connecting, just thinking that no one more will connect because of the holidays today.
**Vinod Vydier** 00:45 Yes, yes, I am also not sure.
Yeah. I didn't see any message on the channel. So I said, Okay, let me
see. And and Bryce is created a few prs that we could discuss.
**nacho** 00:59 Yes, yes, that's true.
But yeah, but he's.
**Vinod Vydier** 01:03 In the world.
**nacho** 01:03 Not joining.
**Vinod Vydier** 01:04 Oh, he's not joining. Okay.
**nacho** 01:06 Yeah, he wrote on the Channel. Yeah, but it has been a bit noisy. The channel so
**Vinod Vydier** 01:13 I I didn't see that as I had a doctor's appointment in the morning, so I.
**nacho** 01:20 Okay, yeah. Ari is also joining.
**Vinod Vydier** 01:22 Oh, Arizon, okay, hey? Ari.
**Ariel Demarco** 01:26 Hey! All.
**Vinod Vydier** 01:28 And.
**Ariel Demarco** 01:37 Now it's called the Us. But
wanted to know if you guys.
**Vinod Vydier** 01:42 Yeah.
**Ariel Demarco** 01:42 And to join.
**Vinod Vydier** 01:43 There are other countries outside of us, too.
who who probably do not have a holiday right? Right.
**Ariel Demarco** 01:53 Oh, I see Argentina to more recently.
**Vinod Vydier** 01:59 Oh, let's that.
**nacho** 02:00 Journal of you're located! Located in Buenos Aires or.
**Ariel Demarco** 02:05 Yeah. I'm in Buenos Aires.
**Vinod Vydier** 02:10 I loved Buenos Aires when I was
Palermo.
Dog bunch of other places. Yeah. I stayed there for 2 weeks and planning to oh, bye.
**Ariel Demarco** 02:32 Turns out what a lovely place!
Exceeding.
**Vinod Vydier** 02:45 I I love the fact that you know. You guys have so many places to eat, and they all start late, unlike
here in the Us.
So do do we? Should we wait for Bryce for next week, so we can discuss the peers that he has, or we can talk about other things.
**nacho** 03:12 Yeah, as you.
Yeah, I will put my camera as you as you wish. If you want to.
I have updated the document. Now we can't.
If you want to talk about something of those. Or just review.
Yeah, if you want to talk about the topics quickly.
**Vinod Vydier** 03:36 Yeah.
**nacho** 03:37 R, yeah. So let me.
So this one.
yeah, I have just copied things. So
Roadmap from last week the roadmap is created.
Alorita said that he had created one.
Have you checked this.
**Vinod Vydier** 04:07 Yeah, she, I think, created a project under the yeah. So she has.
yeah, that's a good idea to have for anyone coming in. It's right on the repo.
**nacho** 04:20 And there are some topics here.
Should we update?
Yeah, should we think about updating our
development task here? It looks like Bryce has already added that.
**Vinod Vydier** 04:41 Yes.
I mean, as we is, there is no way to automatically update these things right? Because what happens is when you don't do it regularly. Kind of
goes out of sync.
**nacho** 04:52 Oh, so you think it's updated directly from the project.
**Vinod Vydier** 04:59 I don't know if there is a way to do that.
but because I I feel anything that is not
you know, unless someone has to, you know, like, has to update the date. Yeah.
**nacho** 05:14 805, for example, is here metrics, local warning arrested.
Yeah, it looks like it's somehow synchronized.
**Vinod Vydier** 05:30 Interesting.
**nacho** 05:31 I don't know if oh, it's added to the project here.
Hmm!
So maybe $10.
**Vinod Vydier** 05:42 So I think you can link it very easily, just by.
**nacho** 05:46 Okay, yeah. You have to add them to the project. Right?
**Vinod Vydier** 05:48 You know.
**nacho** 05:49 Early if you oh, I had not signed in. Okay, yeah, yeah. That's why I cannot see that here.
Okay, now I am.
So then.
no, okay. So then, just adding, here we can add to the roadmap.
**Vinod Vydier** 06:21 Yup! Yup!
**nacho** 06:22 Okay? Nice?
Okay, yeah. Then that's that's ready.
okay. Stable metrics.
Feature review related to this.
I think Bryce created a Pia to change all the metrics.
**Vinod Vydier** 06:58 You.
**nacho** 06:59 Also.
That's a huge huge.
She's another,
No, this is no.
this is new topic. Sorry it's related, but I think he has been reviewing some of these. But maybe he needs some.
Okay, yeah, that's nice.
Yeah. The Swift 6 support with anything interesting to add.
I think. Yes, we talked about it, but.
**Vinod Vydier** 07:49 No.
**nacho** 07:50 Nothing really clear cocoa pear port is big failed.
We released a new version. Right?
Do we know if that fixed the post spec, or you created this one also. Ari.
**Ariel Demarco** 08:10 Yeah, I agree with that one. It seems to be failing.
I've been investigating why, it could be failing
found out that probably the synchronous sometimes might not be working.
And
and and maybe one of the things that would be good to do is not only fixing this, but also.
you know, in in the to do so, I added, like ensure that the failure of pushing a single pod doesn't really break the whole system.
and the other one is that we can rerun this eventually.
So if it's a failure, because the cache of the cocoa pulps, cocoa pulps spec repository is not updated or the Cdn is not updated, or something like that. We can run it afterwards, and probably it will work.
So I think that those are the most important things we can do to make this stable.
**nacho** 09:14 Okay, yeah.
we'll add this to here.
Okay, performance changes in the SDK span. That's been finished and merged.
And also it's released. Right? What did we create our release? Yes.
**Vinod Vydier** 10:06 Yes, I think so. Yeah.
**Ariel Demarco** 10:08 Yeah.
**nacho** 10:13 This was
61.
Okay, yeah.
The span apa not finished. Still.
I would like to do it before version 2, if possible.
But yeah. Okay. New topics for today.
How far you pr, from more price? This will need
review. And he asked for that also.
So yeah, this one.
It only has changed 271 files.
So this is, gonna take some time he has several commits also.
But yeah, let's see how it behaves with so many changes.
Because, yeah, the web usually takes a lot of time.
Yeah. And there are also some statistic changes
that always make it a bit more difficult. But there is, you know, when reviewing. If you review here, you know you, there is an option here right to remove the
tabs.
And this pieces hide white space. This one. Okay, yeah, this one.
Don't forget about that, because it will reduce the number of changes.
Quite a lot.
Okay.
But yeah, this is a big one.
I don't.
**Vinod Vydier** 12:25 Yeah, but that'll be good, too. Yeah, because there are still some people opening issues on the old
metrics and so on. Right? So.
yeah, this would kind of override that.
**nacho** 12:35 And he also has updated some, not only the metrics itself.
**Vinod Vydier** 12:40 Oh!
**nacho** 12:42 But also sorry I should.
but also the exporters.
**Vinod Vydier** 12:57 Yeah.
**nacho** 12:59 So, yeah, that this will take some time for sure.
**Vinod Vydier** 13:04 So did you remove the Prometheus exporter too?
**nacho** 13:10 Replace the. It has also updated the pro messages, but.
**Vinod Vydier** 13:15 No, not the.
**nacho** 13:17 To use the new one. Yeah.
**Vinod Vydier** 13:18 Yes.
**nacho** 13:19 And the suite metrics also, which is also nice.
**Vinod Vydier** 13:23 It doesn't remove anything. It only updates.
**nacho** 13:25 No. No. Just update. Yeah.
**Vinod Vydier** 13:27 Yeah, okay.
**nacho** 13:29 Also about the other pull request. There is one about the Sync post. Sorry?
No, I don't know what I mean. This one that has not been reviewed.
Yeah, the thing is that.
**Vinod Vydier** 13:45 Another person reviewed it too.
**nacho** 13:47 Yes, it. It has been open, I think today or yesterday, with some updates. Yeah, basically.
I, there was a a sign bus integration like that. It was useful if you wanted to
to see how the spans were created in instruments
and they have updated it. So it uses the new Api, which is nice.
It was updated for the body.
not not for for, but for the bugging and seeing how your response behaved. It was useful and they have updated it.
The only thing is that it needs Ios 15,
which is our minimum version. Currently.
I think that's the main problem with this because, can we?
We are supporting Ios 13. Currently.
we might move to 15, maybe. I don't know. For the version 2.
**Vinod Vydier** 14:55 Yeah.
**nacho** 14:57 But God.
Yeah. So the problem with this kind of things is that we? We are we.
We are limited by by the Ios version.
but it it has this difference, so maybe it can work.
**Ariel Demarco** 15:18 I can gather some metrics in terms of usage, even though we are not like the biggest company. We we probably have a good amount of numbers in regarding Ios version usage, we in that in the new version of the SDK. We also support Ios. 13, but in the old one we support is 11. So we probably have a good amount of data regarding Ios usage.
**nacho** 15:41 Okay.
**Ariel Demarco** 15:43 I can do that for next week.
**nacho** 15:48 Okay, yeah. Great.
Yeah. Let's if you want.
There is also this one to review. This is simpler, and it's a.
**Vinod Vydier** 16:02 Yes, but but can you not add like, if statements for I was 15,
so only for ios 15, use this new version of
**nacho** 16:11 Yes, the it's.
**Vinod Vydier** 16:12 Simple posture.
**nacho** 16:12 This is what it's doing here. Yes.
**Vinod Vydier** 16:14 It could. Then it should work right it should. It should also work for the older versions. Then.
**nacho** 16:20 Yes, it should work. It just seems here the difference.
**Vinod Vydier** 16:23 You know.
**nacho** 16:24 So it uses one or the other. So it should work. You want to. Yeah.
to take a look into that.
There are someone already did some review.
Yeah, it's they're both from.
Yeah. So yeah.
**Vinod Vydier** 16:45 Think Natalie also had another pr before. Yeah.
**nacho** 16:50 Yes.
and that for the Prs. I think that's all, and related to issues.
**Ariel Demarco** 17:08 I think the only one is the one i i created.
**nacho** 17:12 He's 1.
**Ariel Demarco** 17:13 I can take a look at that one. If if you guys want.
**nacho** 17:17 Yes, sir. Do you want
to have to be assigned here?
You can assign yourself. Yeah.
**Ariel Demarco** 17:27 Okay, cool probably start with investigation, and then we'll try to add some sort of resilence to the to the job.
**nacho** 17:40 Okay, great.
For the rest, these are just
tasks that open that, I think. Bryce open. Yes.
Yeah. Another one who's has problem with with the data Compression Library.
yeah, there is also
another option here that I have been thinking, is the import. Only a statement. Do have you seen that Ari.
**Ariel Demarco** 18:14 Yeah, yeah, I have that in my SDK, the implementation on the.
**nacho** 18:19 Yeah, I don't think any SDK can live without that.
So should be, yeah. But the problem is that here we have a
we. We have that data compression in our package as a different
we. We have also another branch with that. But we have that as a different package right?
The data compression is in a different package.
**Ariel Demarco** 18:47 Yeah. But I think the problem is not the package itself. It's it's the the target itself. It's a product.
**nacho** 18:54 Okay.
**Ariel Demarco** 19:03 I think that it's the same problem we had with the
I don't. I don't remember if the it was this one, but
I think we already discussed this, that maybe on on 2 point O would be good to rename
hotel. Yeah, hotel or open telemetry.
**nacho** 19:23 Yeah, because.
**Ariel Demarco** 19:23 Conflict.
**nacho** 19:24 It's because we are we. We have a product, not not because we are importing and exporting with that.
**Ariel Demarco** 19:31 You.
**nacho** 19:32 Yeah, okay, it's the product name, not the yeah. Sorry.
Yeah. I was thinking about that as a solution. But it's it won't be.
Yeah, I think. Version 2, we have to update that definitely.
I there is a branch. I I will rebase
the branch, and we'll tell them to use the branch if they can, at least temporary.
until we release version 2, and then
Happy dumped up.
Oh, sorry.
Okay,
So the price that lands directly also uses data. Compression library. Oh, oh, the one that is here.
Yeah.
**Ariel Demarco** 20:42 It's definitely a problem on, on, on, spm, like.
**nacho** 20:46 Yeah, yeah, definitely.
**Ariel Demarco** 20:48 Because modelization should include.
like the org and the actual direction to to that module, because data compression seems like a common name to use. I mean to my, to my thoughts.
So they launched. Luckily we'll probably have problems with other Sdks as time goes by, because data compression seems.
**nacho** 21:13 Yeah.
**Ariel Demarco** 21:13 Just like a generic name.
**nacho** 21:15 Yeah, that's right. Yeah, yeah.
yeah, there is nothing we can do there except for version, 2, yeah.
Cocoa pods releases broken. This is the one that was handled by the other. Yeah, and I think we have
the rest already handled.
Any any other topic, any other thing you you you want to talk about.
**Ariel Demarco** 21:58 Okay, from my end.
**Vinod Vydier** 21:59 I'm good.
**nacho** 22:01 Okay, then I think we can end early today and leave be not celebrate.
Juneteenth.
**Vinod Vydier** 22:08 Yes.
**nacho** 22:09 Okay.
**Vinod Vydier** 22:10 I'm wearing the T-shirt. But I I'm actually in the car. So.
**nacho** 22:15 Yeah.
**Vinod Vydier** 22:17 Alright.
Talk to you guys.
**Ariel Demarco** 22:19 All right, guys.
**Vinod Vydier** 22:20 Later next week. Yeah. Have a good weekend.
