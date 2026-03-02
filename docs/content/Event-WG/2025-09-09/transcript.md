SIG: Event WG
Date: 2025-09-09
Duration: 38 minutes
Zoom Recording URL: https://zoom.us/rec/share/7mrqsuaj4LwYjulI22ZVFXO5kMPvIJzQceDaFb0lAh4McgJqv71DvI3LWjOufE1v.tHjatHywDRDfY_g1
============================================================

## Zoom Recording Transcript

**Liudmila Molkova** 01:36 Hello, hi, Robert.
**Robert Pająk** 01:41 Hello, hello, I'm just rereading, Trask's PR, and this bike… is by Scudding? Skadjink? I hope that you pronounce it, I'm not sure.
Like, like, like…
**Liudmila Molkova** 01:55 Which pair?
**Robert Pająk** 01:56 Excuse me, the… about means, severity, and trade days.
And I noticed, but basically the section when we have a little… a little disagreement is kind of redundant, because Trask already had it even more specific. Oh, Trask is here called.
has it even more specific description in the EMIT record, and…
and enabled, and I'm thinking that maybe just dropping it would be the easiest way. Hello, Trust.
We cannot hear you, unless… No, we cannot hear you.
By the way, thanks a lot for your review.
on the… I think…
Yeah, it was helpful, because we could discuss it today with Daniel, which I remember I was checking the OTAP, all comments, and I remember the whole… basically, the whole discussion was coming from Daniel Andreas. This may a must, and I was checking the OTAP comments everywhere, etc.
So, I think it will simplify a lot, because when I…
Yeah, because when I was thinking where I would put these APIs, you know, probably I'll need to create those two types, like simple attributes and extended attributes, and I thought, oh, business, it would be so hard to read and write it, so it's readable, so yeah.
**Trask Stalnaker** 03:34 No.
**Robert Pająk** 03:35 And we can see you.
**Liudmila Molkova** 03:36 Yeah!
**Trask Stalnaker** 03:37 It's amazing. Technology's amazing.
**Liudmila Molkova** 03:41 Yes!
**Robert Pająk** 03:42 And we can see all…
**Trask Stalnaker** 03:48 So amazing that my calendar never, ever reminds me that this meeting is starting.
Apologies.
**Robert Pająk** 04:00 No, no worries.
**Trask Stalnaker** 04:06 I will pull up… our… Agenda…
If for no other reason than to document that we were here.
Hey, look at that. Same… Fox.
Alright, Robert.
What would you like to chat about?
**Robert Pająk** 04:44 Firstly, I think first, the meme, severity, and trace-based PR.
I think it'll be fostered here.
If you'll just show the changes, because the description is there.
So, I started to read it just before this meeting again, because basically, yeah, it's about these comments here.
And I rechecked all PR again, and I noticed
that basically, if I understand correctly, the section is about being repeated later in the log record, emit a record, and enabled. I think you, after… later you added more clarification later below.
Even below, below, in media record, and it will be here.
So, mu severity will… so, this is basically what it's already describing.
And same in enabled, you have similar section.
And in my opinion.
this is enough, and we can probably maybe even, you know, just remove this, I think, unless I have missed something, this is basically a duplication of the same.
**Trask Stalnaker** 06:11 Okay, so I think there's two… there's two things to discuss. One is the duplication, the other is the must versus should.
Because I think I had should here, and I think I accepted your, Robert, your…
proposal to change it to must, but then I realized…
when I was doing this, that we… there was sort of… Lyudmila had wanted that distinction.
By default, and so… .
**Liudmila Molkova** 06:49 So we… we and Robert, we violently agree on the behavior. We don't agree on what's a human-readable explanation of this behavior.
**Robert Pająk** 06:58 I think this one is variable, because here it's set explicitly, is specified.
If it's specified EN00, then it must be dropped.
is the most precise way, because I even wanted to say that the previous statement
The first statement is in contradiction with the second, because you do not have this specified in the previous section.
I was also thinking about nitpicking this one, that one statement says that below zero and then must not blah blah blah, so basically these statements are in conflict, but I think if
If we have this one, and a similar in enabled, then I think we can Basically, remove the section.
This whole.
**Liudmila Molkova** 07:44 Or we can… Go ahead.
**Trask Stalnaker** 07:47 We don't say… we don't say below what to do with unspecified severity.
Down east.
**Robert Pająk** 07:56 Get it, Jess.
There's nothing.
**Trask Stalnaker** 08:02 Oh, I see what you're saying. I see that it must be dropped.
Otherwise, like, it doesn't do anything.
**Robert Pająk** 08:11 Exactly.
**Liudmila Molkova** 08:12 Otherwise, we will… we might come up with some… something in the future, so… Yes.
**Robert Pająk** 08:19 We've sub… separate… you know, field or whatever. Drop unspecified or whatever.
**Trask Stalnaker** 08:27 So, Robert, what do you feel about adding a… and I understand
Your point that this is self-sufficient?
**Robert Pająk** 08:36 Yes.
**Trask Stalnaker** 08:36 But to address… Readability… What do you think of…
adding, one more sentence here saying what to do with zero, like, that it doesn't… should do nothing if it's…
**Robert Pająk** 08:52 It's good for… is it good for me.
**Trask Stalnaker** 08:59 And would we say must?
**Robert Pająk** 09:01 do nothing… Like, here we say already that it is only for the specified.
So, it does not… the next sentence does not have to be normative. It will be just, you know.
Adding clarification. This sentence here is self-sufficient.
And I think it's the same for enabled. The only problem in enables, if we scroll down a little bit.
Possible problem is that here you say that only the provided separability is specified.
I will probably try to use the same language as above.
It's specified, and, in, in parentheses, not, not zero.
the provided It's specified at least zero.
**Trask Stalnaker** 10:05 So, here…
**Robert Pająk** 10:08 I just copied.
is specified E not zero.
I think it's more… a little bit more…
The provider's severity is specified.
**Trask Stalnaker** 10:25 Turn false, when… Provided severity…
**Robert Pająk** 10:32 is specified.
**Trask Stalnaker** 10:37 I understand, yes, yes, yes, yes, I like that. Yep. It's specified.
**Robert Pająk** 10:42 Yes, it does this.
and Western.
East, remove is.
I see this up here.
some more correct in this, yeah.
**Trask Stalnaker** 11:15 Yes, okay, yes, we're matching, we're matching now.
I like that.
**Liudmila Molkova** 11:27 picture.
**Trask Stalnaker** 11:29 Okay, and then… up here…
**Robert Pająk** 11:33 First scenario will remove the whole section here.
**Liudmila Molkova** 11:38 Yeah, so in the way it's…
**Robert Pająk** 11:41 Described below. From 200 to…
Yeah, I will just drop this. Yep.
**Liudmila Molkova** 11:50 I mean, we still need… we still need to say the rules are described below, somewhere.
And…
Logically, it makes sense to move the rules from the logger image record to the enabled, and then link
log record emit to the enabled. Because you would… that's what you would do in the code, right? You would implement this enabled once, and then you would check it.
**Robert Pająk** 12:17 It's… but, we have the same pattern already for disabled.
**Liudmila Molkova** 12:25 So if you look at the disabled.
**Robert Pająk** 12:28 It's not really a saint exactly.
How it, how it, yeah.
**Trask Stalnaker** 12:40 I see. If not, I see the, indicating…
Defines configurable aspects. Yeah, this is… defining that.
And this is the behavior disabled.
I mean, it kinda does, though, here.
**Robert Pająk** 13:01 Boom.
**Trask Stalnaker** 13:12 What do you think about just…
copy-pasting that same language is specified, i.e. not zero, and is less than the configured…
**Robert Pająk** 13:23 At least it's the same sentence, which we can copy and paste, you know, as a note-finding…
**Trask Stalnaker** 13:28 everywhere.
**Robert Pająk** 13:29 Everyone, different terminology and different ways of saying the same.
**Liudmila Molkova** 13:34 Yeah, that sounds good.
**Trask Stalnaker** 13:41 Is… specified…
**Robert Pająk** 14:03 So, see the second line?
No, just in the second line, specified ENO.
**Trask Stalnaker** 14:12 Oh, yes, yes, thank you.
added.
**Robert Pająk** 14:25 Oh, thank you.
**Trask Stalnaker** 14:35 And so, okay, so what do we want to do about.
**Robert Pająk** 14:38 we can… we can change it to a non-normative statement. It's not affected by this parameter.
**Liudmila Molkova** 14:46 Yeah, that's good.
**Robert Pająk** 14:50 Yes.
I'm not affected by this parameter.
**Trask Stalnaker** 14:57 By default?
**Robert Pająk** 14:59 just…
**Trask Stalnaker** 14:59 Remove that.
**Liudmila Molkova** 15:04 I'm finding their way.
**Robert Pająk** 15:05 Never.
**Liudmila Molkova** 15:05 Refactoring of this.
**Trask Stalnaker** 15:10 Yeah, because if we add another option at some point for that, then that would be… affect that.
There was one other… Oh, okay, and then, so we, we only, I think…
It's okay, we would only have that one explanation there. Okay, yes.
So, I'm going to… Commit…
And we'll resolve… resolved…
**Liudmila Molkova** 16:45 Wonderful.
Yay, we didn't spend time bike shedding mouse versus shoot! I'm proud of us.
**Robert Pająk** 16:56 Yep.
**Trask Stalnaker** 17:08 Let's see… I'm going to… I like trace-based.
That's okay.
To resolve it.
Alright.
Have another look whenever you have time, Robert.
Thank you for… Bringing that.
**Robert Pająk** 17:30 I just run Copilot running short, because it finds nothing good.
**Trask Stalnaker** 17:36 Nice
Yeah, that's actually good. I saw you were, doing that on your PRs.
Let's see, reviewer… Copilot…
All right.
So we… Discussed this.
What's next?
Did you have something else in flight?
I don't have an update on my Java… Prototype.
For the complex attributes.
I think that…
Yeah, I… I was playing around with it locally after we chatted, and I think
Anyway, won't waste our time with that, I will.
Push something new, and we can discuss.
Next week. Also, Jack… Jack has at least started checking in on Slack.
So, hopefully he'll… be back,
Actually, he said he could check some PR, so once I have something that I like here, I will ask for his input.
**Liudmila Molkova** 19:31 Cool. Do we wanna…
discuss something about, Robert's PR, bringing that up to the spec, or Robert, you're good for now.
**Robert Pająk** 19:43 I think I would like to double-check one thing.
But just a heads up regarding this valid feasibility, some people already said that they are okay.
So, you can see a few… a few issues close.
So, the most important, I think, is Java. I hope Sijo will also react to Rust. I will give him some time, so maybe I'll ask him next week if he doesn't respond, but he's very usually… I think he's even…
He's even following me on this cup, because sometimes he's reacting very soon, even if we just have let him go.
So, yeah, what's… And I… and during the SPAC meeting.
the most important thing was the Java thing, right?
So, I think that… whatever will be in the spec PR, Probably, we shouldn't merge it
until it's double-checked with Java.
Giving also is the most important language.
Regarding this PRO DOMI, I added… have you seen my summary, in… regarding this?
Maybe I'll just add it.
**Liudmila Molkova** 20:55 I haven't know.
**Robert Pająk** 20:58 This is one thing which I would like to double-check.
I'll just edit the notes.
Second from the top, yep.
So… I think there are two opening… Too often conversations.
One is here… So maybe let's start with this one, because it's…
maybe not easier, but it's more about how to define it. So, initially, I did it like you proposed, and this is in this end, like, end result PR. I didn't do it because I thought that this
map swing any, Some of the types are still development.
Are this sweet unlocked?
in development state. Like, the one where… basically, I added these types, you know, in development state, while map string, any is already stable.
So, if anything… so, I think it's more about being,
perfectionist, perfectionist to be saying, you know, just to have, it very clearly that this kind of attributes were already supported in a stable way in the logs data model.
So, it's basic about it, but the end goal is to just have attribute collection here.
Instead of this.
**Liudmila Molkova** 22:48 I see, so essentially the map string of any was implemented in some languages in some way.
Yes.
**Robert Pająk** 22:58 And he's already stable.
**Liudmila Molkova** 23:00 And it's already stable, and when you're in attribute collection, it's not stable, so…
We can also say on the attribute collection that these types are stable for logs, and then development for everything else.
Which is true, to some extent.
It, I, I mean, yeah.
**Robert Pająk** 23:22 Basically, my plan is that when those types are stable, I will remove this, any definition and map string any definition from the rocks attribute, and just remove this OR.
**Liudmila Molkova** 23:33 Okay.
Okay, because they are the same.
**Robert Pająk** 23:36 Yes, exactly.
And regarding this one, you can see my last statement.
This was the summary.
**Liudmila Molkova** 24:14 Well, I think we need to have some, like… so, what OTAP says, right? In certain places, you must expense must take complex attributes, right?
Entities identifying attributes may… if somebody wants to build an API for entities that's type-safe, they can prevent
complex attributes, from being added as identifying attributes. They can do this, right?
and… It's important to have some distinction in the spec that allows them to do this.
**Robert Pająk** 24:52 The thing is that, if I remember, if I understood correctly, nobody cares about it.
And I think specifying this would be just very cumbersome and very hard to…
specify those distinctions. Because, Daniel said that if other languages will support it, for example, Go will support it.
collector supports it as well already, then people will complain that, for example, in JS, they're not able to do it, and they do not want to have this problem, so they would just support this, even though they initially were against the idea of extended attributes, but once
That is that once we agreed that we'll extend the attributes, he preferred to just add it consistently everywhere.
So he was…
**Trask Stalnaker** 25:41 So it sounds like we… we added this language to make…
**Robert Pająk** 25:47 If it's possible.
**Trask Stalnaker** 25:48 Folks come comfortable that they could…
**Robert Pająk** 25:51 Yes.
**Trask Stalnaker** 25:51 Decide otherwise, but it sounds like they have…
Decided that, given the outcome, that they would just align I mean, I think it…
**Robert Pająk** 26:04 I, I think it's…
**Trask Stalnaker** 26:06 Fine, as long as we call it out here, make sure that…
books are… like, I think we can…
I don't think we have to implement the OTEP.
Precisely, as long as we call out differences and make sure that You know, we should get…
Extra approvals from those folks, just to… Be clear.
**Liudmila Molkova** 26:36 Okay.
Okay, so as long as everybody's fine with, erasing the difference.
here and in other places, so I'm not going to push back on this.
**Robert Pająk** 26:56 So I should probably document in the PR description.
Just to make it clear.
**Trask Stalnaker** 27:03 Yeah.
**Liudmila Molkova** 27:06 And in particular, it sounds like that Daniel and Jack would be the two people that should at least not block, ideally approve.
**Robert Pająk** 27:17 Okay, oh… Alright.
**Liudmila Molkova** 27:21 I mean, don't consider it something you need to push for, right? We or all three of us would probably, be on the same goal.
**Trask Stalnaker** 27:31 And I'm assuming this.
**Robert Pająk** 27:34 Fair enough.
**Trask Stalnaker** 27:34 would we… merge this before… the feasibility…
**Robert Pająk** 27:42 I just remember one thing regarding Jack. I remember Jack… In the LTEP.
was not against for this proposal. I remember
I can find it quickly. Can I share my screen?
Sure. Unless… unless… There is something you…
**Trask Stalnaker** 28:01 I mean, I agree with you that that was not a sticking point for Jack.
**Robert Pająk** 28:07 But it would…
**Trask Stalnaker** 28:08 Still be worth, you know, and I think with the Java prototype that I… Hob is…
applying it consistently, and I don't think…
I don't think Java would make that distinction. I don't think we can really make that distinction.
**Liudmila Molkova** 28:28 Well, the… yeah.
The only reason I brought it up is that
So, like, there are proposals on entity API SDK.
If it has convenience to identify an attribute.
Not attributes, singular.
**Robert Pająk** 28:45 I was out here.
**Liudmila Molkova** 28:46 And…
**Robert Pająk** 28:47 Very exciting!
**Liudmila Molkova** 28:48 It… the convenience… It's weird to provide the convenience for the complex attribute on entities.
**Robert Pająk** 28:57 Yes.
**Liudmila Molkova** 28:58 But, then we are leaving it up to somebody who reads the spec to…
And how to implement this convenience, and it's fine. If they really want to dig, they can look into the OTAP and find answers there.
**Trask Stalnaker** 29:20 Do you, is there a specific Language where you're seeing that
They might want to have that distinction on entities.
**Liudmila Molkova** 29:33 Not a specific language, more like whoever implements a convenient entity's API rate.
**Trask Stalnaker** 29:41 Okay, just because I… I mean, I assume… I have to… I haven't looked, but I have to assume that in Java, we would…
Want to reuse our existing attributes.
class.
**Liudmila Molkova** 29:58 Absolutely, but when you say you have span set attribute, right?
And if you have entity set attribute, you might not need to provide convenience for each of the
attribute types.
**Trask Stalnaker** 30:15 Oh, I see. So in Java, okay, I can see. In Java, that doesn't help us, because we already have the generic,
set.
We only have… Convenience ones for… Specifically type… primitives, we are…
I'm not proposing we would even add that for…
Because we just have the set attribute, attribute key.
**Liudmila Molkova** 30:50 I see you. Okay, so I probably misremembered that you had specific ones for… maybe you deprecated them at some point.
Anyway, I think we can consider this discussion resolved from my side. If you would have prototype.
If Jack, is on board with this prototype, it's a good signal that he is fine.
Was the same type being reused everywhere, which means entities and metrics and whatnot.
**Trask Stalnaker** 31:21 Yeah, just to show you, so, like, you're thinking of these, overrides for string, double, boolean.
But we also have this one.
And so we can't get away from… we might not add convenience methods for… Right.
that, but we can't get away from this one. This one will have to be implemented everywhere.
Because generic… at least, we can't make it type-safe to prevent people from adding any attribute key.
**Liudmila Molkova** 32:02 Yeah, okay, so then maybe what can save us and resolve the last, slightest concerns I have. So, we have a language in this ODAP saying that we should
document that complex attributes are discouraged in general, period, right? So it essentially means that whatever Convenience API you built, you probably should not have convenience API for complex attributes anywhere.
**Trask Stalnaker** 32:28 Right.
Right.
**Liudmila Molkova** 32:30 And if we include this link…
**Trask Stalnaker** 32:33 At least not for those… Pieces, like.
Span… complex attributes on events and spans wouldn't be discouraged.
**Liudmila Molkova** 32:45 date… The language and data, they are discouraged.
everywhere.
**Trask Stalnaker** 32:51 Really?
**Liudmila Molkova** 32:52 Yeah.
**Robert Pająk** 32:53 I mean… I don't know why it was disclosure in Spanish, to be honest.
**Liudmila Molkova** 32:59 Because, the language says Hawaii?
Let me… Yeah, you're looking for it.
**Robert Pająk** 33:10 I think the reason why people didn't want to access to span events is just some people wanted to deprecate span events, so they… Yeah, no, so scroll down, find.
**Liudmila Molkova** 33:23 Simple attributes should… yeah, this note below.
**Robert Pająk** 33:31 No.
**Trask Stalnaker** 33:32 Not index. Oh, okay, okay. The criteria. Okay, okay.
It's a good explanation. We should… yeah, the… I mean, we should definitely carry this over…
into the… your PR, Robert, if it's not already…
**Robert Pająk** 34:00 I'm just not sure if… Because this shoot is about the usage, so…
SDKs should document, or languages should document.
**Trask Stalnaker** 34:14 Yeah.
**Robert Pająk** 34:16 Something like that, along these lines, okay.
**Trask Stalnaker** 34:18 Yeah.
I think we have some precedence for that in the spec of saying Like, should document something.
**Robert Pająk** 34:27 Yes.
**Liudmila Molkova** 34:41 Cool, so then, effectively, whoever builds Convenience API, the language like this would be enough for them to question how much convenience they want to build around complex attributes.
**Trask Stalnaker** 34:58 Yeah.
**Liudmila Molkova** 35:01 Robert, do you want me to leave a comment about this, or do you remember?
**Robert Pająk** 35:06 We would love to.
**Liudmila Molkova** 35:07 Okay.
**Robert Pająk** 35:08 If you are here… if you are already… Have it opened?
**Liudmila Molkova** 35:13 I'll leave a comment, thank you.
**Robert Pająk** 35:15 Thanks.
**Liudmila Molkova** 35:19 On this one, I think I can link the Python prototype I had for this issue, and with the
A summary of what we discussed.
There.
**Trask Stalnaker** 35:34 Cool.
**Liudmila Molkova** 35:59 Cool! It's coming together!
**Trask Stalnaker** 36:04 Yeah, and so this one, this is pulling out the Piece of this.
Got it.
And this is not related to logs, so we don't have to debate that here.
**Robert Pająk** 36:24 No, not at all. I first need to double-check with the auto go-seek.
**Trask Stalnaker** 36:33 Alright.
We were going to do a blog post.
about…
**Liudmila Molkova** 36:44 on…
**Trask Stalnaker** 36:46 Complex attributes coming.
And I think you've done all of the free rec…
Robert, I think we were… we, I don't think we… necessarily…
Need to wait for this to be merged.
We just wanted it open to be able to point to it.
**Liudmila Molkova** 37:15 I can draft a blog.
with U.S. quarters, and you would share your thoughts on what's missing, what should be there.
**Trask Stalnaker** 37:26 That would be awesome.
**Liudmila Molkova** 37:28 Cool.
**Trask Stalnaker** 37:51 Anything else?
Oh, I saw this got merged.
Yay.
Event name.
**Liudmila Molkova** 38:05 It was back.
**Trask Stalnaker** 38:17 Alright.
Should we call it?
**Liudmila Molkova** 38:21 Yeah, 20 minutes early. Awesome.
Thank you all.
**Robert Pająk** 38:26 Congratulations.
**Trask Stalnaker** 38:27 Bye.
