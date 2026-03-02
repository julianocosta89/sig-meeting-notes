SIG: eBPF instrumentation
Date: 2025-12-10
Duration: 26 minutes
============================================================

## Zoom Recording Transcript

**Rafael Roquetto** 00:57 Ciao ragazzi.
**Giuseppe Ognibene | Coralogix** 01:02 Alright, office.
**Rafael Roquetto** 01:04 How are you?
**Giuseppe Ognibene | Coralogix** 01:05 Find you.
**Rafael Roquetto** 01:07 Fine, fine, thanks.
**Giuseppe Ognibene | Coralogix** 01:09 I had the chow agati, and I was like…
**Rafael Roquetto** 01:18 I mean, I gotta take the chance to speak a little Italian from time to time.
**Giuseppe Ognibene | Coralogix** 01:23 Fun by me.
Hi, everyone.
**Tyler** 01:30 Hey.
Is, Rafael speaking Italian? Is that what I heard?
**Rafael Roquetto** 01:40 I'm just pretending.
**Tyler** 01:44 Was there just a lot of this?
Cool. How are y'all doing? Looks like we're about ready to jump in here. I don't see,
Nicola, or… Mario, I don't know…
Rafael, do you know if they're able to attend at all?
**Rafael Roquetto** 02:11 I… they haven't said anything that they wouldn't attend, so they might be coming at me.
**Tyler** 02:15 Okay, we can wait a little bit.
**Stephen Lang** 02:17 Nicola's at the dentist, and… Ugh.
Mario is on a conflict, but he might be back in a few minutes.
**Tyler** 02:27 Okay, yeah, cool. No worries then.
Yeah, then I think we're probably good. If you haven't yet, go ahead and add your name to the attendees list. If you have agenda items, go ahead and add them there as well.
And, yeah, we can… we can jump in here.
Cool. Oh, one call-out I did want to make before we started. Steven, I did get that release out last week, or… I think it's last week, and that automation stuff worked really well, so thanks for putting that up, by the way.
**Stephen Lang** 03:03 Okay, great, yeah, so you just did a push on the git tag, and then everything else fell into place?
**Tyler** 03:08 Yeah, like, almost, like, scary, so, like, I went to go create a release, because I totally, like, forgot that we had something like that set up, and it was like, this release already exists, and I was like, what? And it was, like, already there, so, yeah, it, yeah.
**Stephen Lang** 03:20 Okay, cool.
**Tyler** 03:22 Yeah, it was really, really quick, too. Like, it was faster than I could create a release, so, yeah.
**Stephen Lang** 03:27 Awesome, yeah, it'll probably get slower in future if we put some guards in place so that, you know, the workflows only run and, you know, that kind of thing.
**Tyler** 03:35 Right, right, yeah, no, I… but for now, at least, it was, it was great, yeah, and everything seemed to… seemed to work out just fine.
**Stephen Lang** 03:43 Awesome.
**Tyler** 03:44 Yeah, and then, like, if we do, like, binary signing in the future, we'll probably have to integrate that somehow, but that's… that's for a future problem, I guess.
**Stephen Lang** 03:53 Yeah, I've not had a look at that. I don't know if anybody else wants to look in the meantime. I've not had time to check out the cosign… cosign stuff yet.
**Tyler** 04:02 Yeah, probably a next-year thing for me if I get to it then, but yeah.
**Stephen Lang** 04:06 Sure.
**Tyler** 04:07 Yeah. But yeah, cool. Thanks, thanks again, Steven.
Cool. Well, the only thing I had on the agenda was to go over open PRs, which hopefully will spark some conversation, so…
Hmm, I might not be in the right browser.
Yeah, this is gonna be kind of hard to review if I, don't have access. Okay,
Let me switch this up really quick, sorry. I thought I was all ready, but I am not.
Okay.
Cool.
Sorry about that delay. Let's, let's jump in here, then.
Okay, looks better. So…
First up, I guess we start at the bottom. These still haven't had any movement on them, so we probably don't need to talk about those. We talked about those last time. Similar to this hotel collector, this is related to these, two other PRs, something that, just to keep following up.
I know, Steven, we talked a little about this, this MQTT, MQTT, draft. It seems like this is still a work in progress, right?
**Stephen Lang** 05:43 Yeah, that's right, I've got some more code, locally.
I've got, connect packets, parsing, and the headers. I'm just trying to make sure that the, there's a good base for the rest of the packet types to come in. There's about 15 different packet types.
from QTT, I thought I'd try and get the first one right, and the rest of them should fall in fairly quickly after that. But yeah, that's just kind of ticking along.
**Tyler** 06:07 Yeah, yeah, yeah, no worries. That sounds good. So we'll, we'll keep, keep an eye on that, wait for, to switch out of draft mode, and then we'll give it a review. Thanks, thanks for working on that.
Next up, Giuseppe, we talked a little bit about this last week as well, this, uniform debug print message. It looks like there was some feedback, if I remember correctly.
**Giuseppe Ognibene | Coralogix** 06:26 Yeah, I didn't have time again.
I will do it today or tomorrow, but I will follow Raphael and Nicola Suggestion?
I will use the… I will check if BBFSAPrintf is available, and then I will print the function name directly inside the wrapper.
The only problem is that, if…
The kernel doesn't support BPF SNAP printf.
Basically, the log, we will not have the function name.
But I don't think it's a problem.
**Rafael Roquetto** 07:03 Do we know which kernel version is the minimal one?
**Giuseppe Ognibene | Coralogix** 07:06 $5.
5.10.
**Rafael Roquetto** 07:09 5.10, okay. I mean…
it was… for my end, at least, was, just a suggestion. If you think that's not gonna work, then it doesn't work.
**Giuseppe Ognibene | Coralogix** 07:19 No, no, for me it's good also, because, the last… the other solution, it was to write or to code the function name, because there is a problem with,
kernel version less than 5.11 for the number of arguments.
So I think this is the best solution, both for logs and developers.
**Rafael Roquetto** 07:42 Okay.
**Giuseppe Ognibene | Coralogix** 07:45 Okay, thank you.
Cool, alright.
**Tyler** 07:47 Well, we'll keep an eye on that, then.
Next up, implemented trace log correlation. This is something, Mattia, you've been working on for a little bit. Looks like it's ready for review.
Let's see… Loading the reviews. I thought there was a… yeah, there's definitely been some feedback on this one.
Mattia, are you on the call?
**Rafael Roquetto** 08:15 You're, for some reason your microphone's not working.
**Tyler** 08:19 Oh.
Okay, well, hmm.
It… not a big deal. It looks like there's still some feedback on here. I'm guessing what you're saying is you're looking at the feedback, and we'll probably try to update this. So yeah, it looks like this is just looking for some… some update on this.
Double check if you're still here… Yeah, I'm guessing…
**Stephen Lang** 08:50 I think he's dropped off.
**Tyler** 08:51 just…
**Stephen Lang** 08:51 Gonna rejoin, maybe.
**Tyler** 08:54 Yeah, yeah, okay. Well, maybe, we'll come back to this one later if he wants to say something more about this, but, okay.
So add support for pythonasync.io.
Let's see… Mark, this is something that you're working on. I see Mattia's joined again, but maybe we'll go back to it.
I thought I saw Mark on as well.
Yep, there's Mark, okay.
Mark, did you have anything you wanted to add to this, or is there any sort of state, that this is waiting on?
**Stephen Lang** 09:39 Doesn't look like he can hear you.
**Tyler** 09:41 Yeah, okay. You can hear me, right?
**Marc** 09:45 No, yeah, there's a lot of feedback I have to address, so today, yeah, today I was busy with all this stuff. Yeah, yeah, sorry.
**Tyler** 09:55 Yeah, no worries, nothing's blocking, though, it's just a few Right? Yeah, okay.
Okay, cool, sounds good.
Mattia, I see you're back on. Is there anything you wanted to add to this, other than you're working on, follow-up from review?
Oh, I still can't hear you.
Give it a second.
Hmm. One thing, Messiah, if, we'll keep moving on, but, you can always call in as well. I've done this before, it's really annoying, but on your phone, like, you can actually, like, talk that way,
Don't unmute, otherwise it'll… Don't unmute your…
Or have headphones in, I think, is what, yeah, if you're gonna do that, but… Okay.
Okay, jumping on, next up is, support for distributed tracing for Ruby on Rails.
And so, yeah, I think…
This is a cool one as well. I'm pretty excited about this. I don't see Nicola on, I did see… oh yeah, he's at the dentist, I didn't see Mario jump on. So, this just, went up, 3 days ago, I guess. So, it's got 2 approvals. It looks like it's actually ready to merge.
**Rafael Roquetto** 11:21 Don't do it yet. I'm looking into it, and I found a little… some things I would like to say, just so…
**Tyler** 11:29 Yeah, okay.
**Rafael Roquetto** 11:30 Don't, don't merge, don't merge it, don't merge it just yet, yeah.
**Mario Macias** 11:36 Just… just ping me if…
when it's ready to merge, but I guess you have some comments to do, so… okay.
**Rafael Roquetto** 11:44 Yep, yep, oh… Thanks.
**Tyler** 11:47 Perfect. Okay, cool. Yeah, thanks for… thanks for pointing that out.
Next up is, updates, Alpine…
Dependency Express, probably don't need to go over these in this meeting, we can skip over that.
added config template for, that Obi accepts. This is something that was posted by a user I'm not familiar with…
Lee?
It popped up for a second. No. That's LFX.
So, one of the things that they wanted to post was just a configuration, essentially, with all the configuration options, which is something I've done as well. They've added it, unless they did an update that I didn't see. It was just as a YAML file with all of the fields that… with a type, essentially, as an entry here.
I didn't think this was that useful, as this just is, like.
as this changes, this becomes out of date. This is something that, like, is a handcrafted way for, like, users to try to find things, to try to figure out what's going on here.
Another thing that we've talked about in the past, and I think something that I suggested in this PR, was that we should probably use something that's,
a meta, language, a meta-templating language, and that is specifically for, you know, JSON schema or Q. I suggested using JSON schema just because it's used in the, declarative configuration, and this is something we wanted to integrate with in the future, so essentially, if we have
JSON schema that we can integrate with the JSON schema from upstream for the parts that need to be, then I think it'd be ideal. So, that was the suggestion here.
It looks like they're still working on the changes, though.
**Rafael Roquetto** 13:30 Does this, JSON schema… is it what it's… I never use it, is it what it sounds like? It gives you a schema of how the
The configuration file was gonna be.
**Tyler** 13:41 Yeah, essentially,
it's, it's essentially like a meta-language saying… it describes what it accepts and what it doesn't accept. This, it works for YAML as well, but the idea is that, like, each field has a descriptor.
It says, you know, if it's required or not, tells you what the type is. If it's, like, some sort of, like, explicit values that are allowed, you can do that as well.
There's also some, like, higher-order abstractions that you can do with, like, references and a bunch of other, like, structure things.
if you've never used it before, it's, like, it takes a little bit of time for you to find out that it's awful, but also, like, I've looked at a bunch of different, these, like, meta languages, and, like, I don't know if there's a better one,
A new language that came out recently is Q, which is something that is being, like, kind of floated over in the Kubernetes space as well, which I think has a lot of, like, really
Interesting and new novel features for it?
it just doesn't have as much of an adoption, the community's not as large. We went over a lot of this in the declarative config on, like, deciding which one to use. The nice thing about JSON schema is there's a lot of tooling, so when you have these meta-languages like this, you can do validation, so you can take
you know, your configuration, and then immediately pass it in through the JSON schema parser, and, you know, load the JSON schema, and you'll just know if your config is conforming to it or not.
it can do a lot with auto-generation as well. It can generate, like, you know, Go code for particular configuration types, that kind of thing. So there's, like, a lot of tooling around, this, this as well, so…
Q itself is really great, especially in Go, which we're writing in, but it's also, like,
like I said, the developer community is… the adoption's, like, still very early on in that one. So I would… I'm up for all I had there, but…
Yeah, that's the idea. Hopefully that helps.
**Rafael Roquetto** 15:33 Okay. Yeah, that's cool, because,
I'm doing some… something else.
that involves, dealing with OB config files, and for now, I'm generating the OB config, and I have just this big block of code that I manually generate the YAML, based on the other configuration that I have. And I was… I was thinking of a schema, and since we already have that, you know.
That's gonna be awesome once we start using it, because then I can just consume it.
**Tyler** 16:03 Yeah, right? I think that's, like, the holy grail, right? Like…
**Rafael Roquetto** 16:08 And so then, yeah, there's actually, like, a lot of really cool, like.
**Tyler** 16:12 automation you can build around that, because once you have it, and integration, so, yeah. I, yeah, I think, like, Declarative Config is already using this as well, so,
That's how, like, it's defined there, and I think that, like, if we can integrate with that, that's why I'd recommend probably just coming to JSON Schema, yeah.
Cool. Alright, let me start shirding again, we can move on.
Okay,
Next up is update semantic conventions to 137. This was, surprising, reviewing this, how bad, we are at keeping up to date on some of these. But yeah, it looks like this is still failing. I probably wanted to ping… I looked at this last night, just before I left, and
It looks like there's just some…
Something that's not being caught here, or there's some, python Kafka test.
So, yeah, there's probably just still some more updates that need to be done, to make these work, but this is great. A lot of our semantic conventions, were very old, and, like, this is using a lot of the latest and greatest, so I think this is pretty exciting. I, went over it a few times, there's a few manual interventions, that are happening as well.
I don't really remember, but essentially, like, we had old semantic conventions that…
We handcrafted, and now we're… we're not doing that anymore. We're using the… the packaging.
So, yeah.
hopefully, Alex, can work on this soon, because I'd love to get this merged, but yeah,
More to come on that one.
Okay, Mattia, another one you opened up, I think, this morning, if I saw, is, this revert of the PPF Core headers, or BPF Core, read header. Looks like there is some issue here.
**Mattia Meleleo** 18:14 Can you hear me now?
**Tyler** 18:15 I can, yeah.
**Mattia Meleleo** 18:16 Okay, nice. My hairpod stopped working altogether. So, yeah, we were doing some debug today with Giuseppe, and we discovered that the iterator was not working correctly.
So, I tried to fix it, to fix it, but I couldn't find, where was the… the issue.
And then I started bisecting, and I found out that there was a problematic commit.
And then I found out there was a fix in LibPF on the headers that we use.
And yeah, it's working again now.
**Tyler** 18:53 Hmm, okay.
Yeah, I mean, this seems, we already got one approval here. Seems pretty straightforward, I'm guessing.
Oh, I see, yeah, it's just syncing.
Yeah, that seems to make sense. Is there any opposition to this?
**Mario Macias** 19:16 Mmm… no, from here.
**Tyler** 19:18 Okay.
Yeah, okay, well, any opposition to just merging this right now?
**Mattia Meleleo** 19:27 No? Thank you, Meredith.
**Tyler** 19:29 Okay. Thank you.
Yeah.
Okay, cool, alright. Then, last one is, Mark, adding a SQL database hostname, capture for MySQL and Postgres.
**Marc** 19:46 Yeah, Disney's review.
But I'm fixing the… This old test.
So… Yeah, but it's basically adding extra information on… from…
SQL operations, because we don't have the host name now, and… Yeah, it just, a bunch of…
Deferring and capturing… yeah, soft fields of abstracts to get the… the host name of the… Other database.
**Tyler** 20:24 Yeah, okay, cool. So yeah, this is just in need of review, then?
**Marc** 20:28 Yeah.
No.
**Tyler** 20:30 Okay.
Alright, sounds good. Yeah, we'll hopefully take a look at this one then.
Okay, that's, it for open poll requests. Let me double check here. Nothing else on the agenda. I can stop sharing my screen here. Any other topics or issues that people wanted to, bring up?
**Rafael Roquetto** 20:53 I just want to let you guys know I'll be on vacations, and I'm back on… mid to end of January, so, you know, happy holidays to you.
**Tyler** 21:02 Oh, okay, yeah. Yeah, happy holidays. Have a good time off.
**Rafael Roquetto** 21:06 Yep, thanks.
**Tyler** 21:07 Yeah, also on that note, the TC, or the GC, one of them, decided that the last two weeks of the year are, meeting-free, so, all of our meetings have been canceled for the last two weeks already, so I think that next week is our last one, if I'm not mistaken. So just a heads up on that.
Well, cool. Yeah, if there's no other topics people want to talk about, we can end the meeting early here.
Thanks, everyone, for joining. Good seeing you all. Hope, for those that I don't see until the end of the year, have a good New Year and happy holidays. Otherwise, I'll see y'all next week.
**Stephen Lang** 21:51 See you.
**Marc** 21:52 Bye.
