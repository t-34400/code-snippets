using System;
using NUnit.Framework;
using UnityEngine.TestTools;

public class Tests
{
  [SetUp]
  public void SetUp()
  {
    //
  }

  [Test]
  public void Tests1()
  {
    //
    Assert.That(target, Is.EqualTo(expected));
    Assert.That(targetFloat, Is.EqualTo(expectedFloat).Within(tolerance));
    Assert.That(targetBool, Is.True);
    Assert.That(targetNullable, Is.Null);
    // etc.
  }
}
