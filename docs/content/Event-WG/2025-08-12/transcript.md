SIG: Event WG
Date: 2025-08-12
Duration: 20 minutes
Zoom Recording URL: https://zoom.us/rec/share/Ny59TPKBn5vRkInIbyLkKQoEBOpwdDoQaea2zXkJ1f4O9pgdquDXrnJRcz5R9eG-.LiZN7xj6RmUijaUs
============================================================

## Zoom Recording Transcript

**Trask Stalnaker** 00:57 Hey, Robert!
**Robert Pająk** 01:00 Hello, nice to see you.
**Trask Stalnaker** 01:03 Hmm… Let's… Let's see… I want to talk about… Alright.
… I… guessing we won't get Lydmilla since she wasn't in the spec meeting today either.
**Robert Pająk** 02:08 I assume the same. Sure. Austin was also not there.
Jason.
**Trask Stalnaker** 02:12 Yeah.
**Robert Pająk** 02:12 conflict, so yeah, I think we can… served.
**Trask Stalnaker** 02:16 Just you and me.
**Robert Pająk** 02:17 Yep.
**Trask Stalnaker** 02:18 R?
Blog post.
**Robert Pająk** 02:23 So, regarding blog posts, I think we should, … one of the PRs which I created is already merged by Rayleigh, the second isn't merged yet, so I think we should… and I still haven't created the, … once these are done, I'll create the draft PRs, so I think that maybe you have some time, you can create the blog post, but I assume you're busy with other stuff, so yeah, I think… We'll just wait a moment. I'm also out home next week. I'll be only working Thursday this week, so I won't create it.
**Trask Stalnaker** 03:18 So then we want to have draft PRs.
Or Proto and Spec. Proto and spec.
And… And… log… Post. Referencing… draft PRs… Okay.
… Yeah.
**Robert Pająk** 03:44 That's it.
So I can start probably working on this stuff in two weeks.
**Trask Stalnaker** 03:51 Sounds good.
You're out, next week?
**Robert Pająk** 03:57 Yes, and 2 days of this week, so almost starting to… I won't do a lot in one day, yep.
**Trask Stalnaker** 04:04 Nice.
Alright, … For… let's see….
**Robert Pająk** 04:15 emotional.
**Trask Stalnaker** 04:17 I thought.
**Robert Pająk** 04:17 I won't know.
**Trask Stalnaker** 04:18 I think this made sense to me. I'm going to make this update….
**Robert Pająk** 04:23 Is that us?
**Trask Stalnaker** 04:25 ….
**Robert Pająk** 04:26 Back to you later.
**Trask Stalnaker** 04:27 For….
**Robert Pająk** 04:28 Sadass.
**Trask Stalnaker** 04:29 go, so you're planning to, you would implement, say, if this lands in the config.
You would still implement this….
**Robert Pająk** 04:42 Mama.
**Trask Stalnaker** 04:42 declarative configuration. You just would implement it with an Without having an actual logger configurator.
**Robert Pająk** 04:50 Can I continue that?
That's correct.
Back.
**Trask Stalnaker** 04:55 Cool. I don't see a problem with that.
That's not… … the important thing to me is the declarative config.
**Robert Pająk** 05:06 aspect. Yes. Yeah, I talked with Tyler and the whole GoSeq, and everyone has the same preference that the declarative configuration should be, you know, what is best suited for most of the use cases.
Because even if there's any complex stuff, people will just probably need their hands dirty and create a.
**Trask Stalnaker** 05:26 Yeah.
**Robert Pająk** 05:26 Awesome stuff.
That's how we see it.
**Trask Stalnaker** 05:32 Cool, is there anything… have you had a chance to review it in detail, as far as anything that you would… Want to see changed for… ….
**Robert Pająk** 05:47 Before approving it.
… I haven't noticed that it's open. I thought that it says a draft, so sorry that I haven't… I haven't noticed it.
the only one thing which I remember before that, I'm not sure how it's specified right now, was regarding the unspecified, local level. I think that there was some language initially that it will be configurable.
I'm not sure if we… if it's here or not.
Or, yeah, I still… Ludum UI.
**Trask Stalnaker** 06:22 Yeah, that's essentially what, yeah, Lyudmila is asking about. … So… Her proposal is….
**Robert Pająk** 06:32 by default.
**Trask Stalnaker** 06:33 Yeah….
**Robert Pająk** 06:35 Yes.
**Trask Stalnaker** 06:35 shouldn't it?
**Robert Pająk** 06:39 So maybe we should come up with some configuration name?
like, I don't know, … drop unspecified, and I'm not sure, just… But right… yeah, I see, right now it's just one field.
And then it would need to be something more complex.
Then just one value, right?
**Trask Stalnaker** 07:10 Yeah, … But we could… so yeah, I guess it depends on if we want to make it an object here with Two things under it, or if we're okay with… this… And… Then… … Let's see, default config… We could do severity….
**Robert Pająk** 07:36 I think, yeah, I think if it will be something like severity processor.
Then we can have something more It could be more configurable.
Like, we can start with only minimum subverting, you know, specification and unspecified, but in future, interiorly, we could also have, for instance, you know, minimum and maximum If people want to have, for example, different destinations or processing for, for, you know, critical errors.
if they will have treated differently. I do not say that we won't do it, but I think it's more open to extensions and configurability, if it will be just, you know, kind of a severity processor, that you would have a few, like, minimum level, for instance.
**Trask Stalnaker** 08:28 So how, what would you… how does that map to declarative config?
**Robert Pająk** 08:34 Exactly the way that you have it here.
Yep.
And we could have an optional yeah, exactly. Drop unspecified.
Well, yeah, something like that, along these lines.
**Trask Stalnaker** 08:54 So, default config… Severity… Maybe severity threshold?
Severity feels a little….
**Robert Pająk** 09:11 Oh, no.
**Trask Stalnaker** 09:16 Default hit severity settings, minimum.
**Robert Pająk** 09:18 Haven't you got the name somewhere filters, severity filter?
I think in Log4J, there's also this notion of filters, or am I wrong?
**Trask Stalnaker** 09:36 Yeah, yeah, … I don't know what filters are… Filter's not bad.
I'm trying to decide, so in… So, zero and un… Configurable… Trying to understand why….
**Robert Pająk** 10:25 Titles of things?
**Trask Stalnaker** 10:26 You would want….
**Robert Pająk** 10:27 number of the page only looking?
**Trask Stalnaker** 10:29 Zero excluded from the comparison.
**Robert Pająk** 10:31 Go talk to a chair.
**Trask Stalnaker** 10:33 Like, I'm trying to understand the use case for… this.
**Robert Pająk** 10:38 I think the only reason, like, for us in Go right now, we are dropping unspecified, because it's, like, the most verbose level, kind of. Because if I remember correctly, 0 is unspecified, then 1 is, you know, trace, etc, but maybe I'm wrong. I need to double check.
How, how, how developed in the data model.
**Trask Stalnaker** 11:02 It is, yeah, you're right, it is zero, because that's a proto-value, essentially, unspecified proto….
**Robert Pająk** 11:11 Yeah, so… We thought that it's okay, because if it's unspecified, that we can… we'd rather consider it as a trash. That was our conclusion.
**Trask Stalnaker** 11:26 You've sucked.
**Robert Pająk** 11:26 Someone finds it differently.
then they can create their own processor, which, for instance, for certain logger names, like, you know, for example, from Java RA, if you know that you have some logger name and they're unspecified, you can set some default for them, if there is an unspecified.
Some kind of processing.
So, that's why we are dropping by default.
**Trask Stalnaker** 12:09 Yeah, so don't events… Today, a lot of events don't have a… severity… Or is it… are they supposed to… Default… to info.
**Robert Pająk** 12:26 I think… I think it is semantic conventions.
We were talking that we should recommend that events Have the severity number.
I'm not sure if it's there already, or if it's only in the form of a GitHub issue created by Ludomua.
**Trask Stalnaker** 12:46 I guess kind of more what I'm wondering is….
**Robert Pająk** 12:48 I think… I think it's just specified, if I remember correctly.
**Trask Stalnaker** 12:55 Okay, so yeah, you can create… … Oh, Lock Record Builder, that's why I couldn't find it.
**Robert Pająk** 13:25 Yes.
**Trask Stalnaker** 13:26 Right.
Yeah… So, I mean… I… Okay.
So why would you consider it trash?
If it's unspecified.
**Robert Pająk** 13:48 Only because we think that when you're emitting, you know.
We just thought that we would have a semantic convention, that everything should have a severity number.
That's the only reason, just to have this kind of filtering, etc.
**Trask Stalnaker** 14:05 Yeah. It's so… it's a….
**Robert Pająk** 14:07 I think it's more like a… preference.
Rather than anything technically, you know, technical.
**Trask Stalnaker** 14:18 Yeah, I agree with making… I mean, we can do the… we can do a good job in semantic conventions of, you know, I do agree with requiring it there.
**Robert Pająk** 14:27 Yep.
**Trask Stalnaker** 14:28 … But for people who are using the logger, Separately… I mean, most of the logging bridges will… Ascent will require it. I mean, the… We'll populate that.
So it would only be people who are using it.
by itself.
**Robert Pająk** 14:57 Correct.
That's… I think that's why Ludumio wanted to… By default, have… do not filter this one.
**Trask Stalnaker** 15:11 Default not.
**Robert Pająk** 15:13 Sure.
**Trask Stalnaker** 15:14 To, by default, keep it, or by default.
**Robert Pająk** 15:17 Yes, I think that Ludomio wanted to keep it by default, and also.
**Trask Stalnaker** 15:22 I want… yeah, I want to keep it by default, … Only because I feel like that's the least. I agree that there's potentially like, it's not great to have unspecified severity, but I feel like it's the least surprising to users.
Like, dropping stuff.
It is harder for users to troubleshoot.
Versus it shows up, and they're like, oh, why did this show up? And at least they have the data to look at.
**Robert Pająk** 15:56 I think… Ludomi was concerned?
It's about negative values, but maybe I'm wrong.
I think that's why she talks about Xero. I remember that she was considering You know, using also minus ones for something more verbose than trace, for instance.
**Trask Stalnaker** 16:20 Which I think is okay, like, I think… I agree with the negative values being… like, even more verbose, and I agree with… Things above 20.
Being even more fatal.
Yes.
As just the zero value because of our defaulting situation.
**Robert Pająk** 16:45 Because I totally… I'm fine with it, and I agree with this proposal.
**Trask Stalnaker** 16:50 Yeah, the question is how important is this option? And probably we'll need to wait to discuss with Lydnila.
I'm wondering how important is it ….
**Robert Pająk** 17:03 True.
That's true.
**Trask Stalnaker** 17:04 To have that option.
Because if it's… if… if we think it's important, then I agree with making a… you know, kind of a nesting thing here. If we think it's kind of.
**Robert Pająk** 17:17 My… my opinion is that it's not in… Port, probably it's not important, but better play safe.
If it will occur in the future, that it is indeed important.
**Trask Stalnaker** 17:34 Okay, I'll, I'll write up, two different… I'll try to make two different options proposals for what declarative config would look like with that one with it being nested And one without being nested, and we can… Kind of see concretely.
**Robert Pająk** 17:56 Yep.
**Trask Stalnaker** 17:57 Because I agree, it's good to think forward, for that.
Cool. Then, yeah, no rush on reviewing, approving, because, I think that's a good thing to work out, and probably want to discuss that next week with Libnila, and then we can… the next week, maybe we'll… when you're back, we can try to get it into shape to get the log sig approval, and then we can start pushing spec.
Alright.
Shall we call it, then?
**Robert Pająk** 18:44 Quick question, I haven't checked, have you got a… folks accepted at KubeCon?
**Trask Stalnaker** 18:51 … I think I'm only signed… I actually have to… I didn't… What did I… I don't think I submitted… Oh, whoa.
**Robert Pająk** 19:03 A little bit sick.
**Trask Stalnaker** 19:06 What's that?
**Robert Pająk** 19:07 I f- I've, so… I submitted for KubeCon one talk personally, and it's accepted.
Nice. It's in the schedule, so I… the second which I, sent was for the Maintainer's Summit, I think it was called that, like that. It's not… there's no response yet.
**Trask Stalnaker** 19:28 Oh, okay, okay, cool. No, I think the only one that I might be… that I was at… I think there's a two, kind of, … there's the OpenTelemetry general update… But I actually, I think I'm on that, but I don't know if we might swap people around still.
So, yes, I'm not quite sure. I should probably figure that out.
**Robert Pająk** 19:56 Okay.
**Trask Stalnaker** 19:58 So you're gonna go… you'll be in Atlanta?
**Robert Pająk** 20:01 I hope so.
**Trask Stalnaker** 20:02 Awesome.
**Robert Pająk** 20:03 First time.
Second time U.S.
**Trask Stalnaker** 20:07 Right.
Cool, then. Well, enjoy your time.
**Robert Pająk** 20:13 Thanks.
See you.
**Trask Stalnaker** 20:15 See it?
